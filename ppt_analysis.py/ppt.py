from pptx import Presentation
p='/mnt/data/Unit4_AP(1).pptx'
prs=Presentation(p)
len(prs.slides)


for i,s in enumerate(prs.slides):
    texts=[sh.text.strip().replace('\n',' | ') for sh in s.shapes if hasattr(sh,'text_frame') and sh.text.strip()]
    print('\nSLIDE',i+1,':',' || '.join(texts)[:1200])


from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, Flowable
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os, math

out='/mnt/data/Unit4_Quantum_Optics_Exam_QA_Diagrams_Derivations.pdf'

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=24, leading=30, alignment=TA_CENTER, textColor=colors.HexColor('#16324F'), spaceAfter=14))
styles.add(ParagraphStyle(name='CoverSub', parent=styles['Normal'], fontSize=12, leading=18, alignment=TA_CENTER, textColor=colors.HexColor('#455A64')))
styles.add(ParagraphStyle(name='H1x', parent=styles['Heading1'], fontSize=17, leading=21, textColor=colors.HexColor('#16324F'), spaceBefore=8, spaceAfter=9))
styles.add(ParagraphStyle(name='H2x', parent=styles['Heading2'], fontSize=12.5, leading=16, textColor=colors.HexColor('#245B78'), spaceBefore=8, spaceAfter=5))
styles.add(ParagraphStyle(name='Bodyx', parent=styles['BodyText'], fontSize=9.5, leading=13.4, spaceAfter=5))
styles.add(ParagraphStyle(name='Smallx', parent=styles['BodyText'], fontSize=8.5, leading=11, spaceAfter=3))
styles.add(ParagraphStyle(name='Formula', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=11, leading=16, alignment=TA_CENTER, backColor=colors.HexColor('#EEF4F7'), borderColor=colors.HexColor('#B8CBD6'), borderWidth=.5, borderPadding=7, spaceBefore=4, spaceAfter=8))
styles.add(ParagraphStyle(name='QTitle', parent=styles['Heading2'], fontSize=13, leading=17, textColor=colors.HexColor('#16324F'), spaceBefore=4, spaceAfter=7))
P=lambda s,sty='Bodyx': Paragraph(s,styles[sty])
story=[]

class Schematic(Flowable):
    def __init__(self, kind, width=470, height=130):
        super().__init__(); self.kind=kind; self.width=width; self.height=height
    def draw(self):
        c=self.canv; w=self.width; h=self.height
        c.setStrokeColor(colors.HexColor('#263746')); c.setFillColor(colors.white); c.setLineWidth(1.2)
        def txt(x,y,t,size=8,align='center'):
            c.setFont('Helvetica',size); c.setFillColor(colors.HexColor('#172B3A'))
            if align=='center': c.drawCentredString(x,y,t)
            else: c.drawString(x,y,t)
        def arrow(x1,y1,x2,y2):
            c.setStrokeColor(colors.HexColor('#245B78')); c.setLineWidth(1.4); c.line(x1,y1,x2,y2)
            a=math.atan2(y2-y1,x2-x1); L=5
            c.line(x2,y2,x2-L*math.cos(a-.45),y2-L*math.sin(a-.45))
            c.line(x2,y2,x2-L*math.cos(a+.45),y2-L*math.sin(a+.45))
        if self.kind=='laser':
            y=h*.52
            c.rect(25,y-18,75,36); txt(62,y-3,'Pump source')
            c.rect(145,y-23,155,46); txt(222,y+4,'Active medium'); txt(222,y-9,'(laser material)')
            c.line(130,y-35,130,y+35); c.line(315,y-35,315,y+35)
            c.line(320,y-35,320,y+35); c.line(335,y-35,335,y+35)
            arrow(100,y,145,y); arrow(300,y,370,y)
            txt(130,y+42,'Mirror'); txt(328,y+42,'Output coupler')
            txt(405,y-3,'Laser output')
        elif self.kind=='energy':
            x1,x2=80,190
            c.line(x1,25,x2,25); txt(135,12,'E₁: lower level')
            c.line(x1,95,x2,95); txt(135,103,'E₂: upper level')
            arrow(105,29,105,90); txt(121,59,'Absorption',7,'left')
            arrow(155,90,155,30); txt(167,59,'Emission',7,'left')
            arrow(205,90,205,30); txt(218,59,'Stimulated',7,'left')
            txt(350,68,'Photon energy: hν = E₂ − E₁',9)
            txt(350,49,'Stimulated photon matches',8); txt(350,37,'frequency, phase and direction',8)
        elif self.kind=='ruby':
            c.roundRect(75,48,300,28,8); txt(225,58,'Ruby rod: Al₂O₃ doped with Cr³⁺',9)
            # lamp coil
            for x in range(90,360,18):
                c.ellipse(x,39,x+10,85)
            c.rect(65,43,8,38); c.rect(377,43,8,38)
            txt(69,90,'Fully reflecting',7); txt(381,90,'Partially reflecting',7)
            arrow(385,62,445,62); txt(445,48,'Red output',8)
            txt(225,18,'Xenon flash lamp provides optical pumping',8)
        elif self.kind=='hene':
            c.roundRect(65,48,325,34,8); txt(227,61,'Discharge tube: helium + neon gas',9)
            c.rect(55,44,8,42); c.rect(392,44,8,42)
            txt(58,94,'Mirror',7); txt(395,94,'Output mirror',7)
            arrow(400,64,452,64); txt(448,49,'632.8 nm',8)
            txt(225,22,'Electrical discharge → excited He → energy transfer to Ne',8)
        elif self.kind=='fibre':
            c.setFillColor(colors.HexColor('#E5EEF4')); c.rect(25,35,420,60,fill=1)
            c.setFillColor(colors.HexColor('#C7DDEB')); c.rect(25,48,420,34,fill=1)
            c.setFillColor(colors.HexColor('#F9FCFD')); c.rect(25,57,420,16,fill=1)
            c.setStrokeColor(colors.HexColor('#245B78')); c.setLineWidth(1.5)
            pts=[(35,65),(90,65),(135,77),(180,65),(225,77),(270,65),(315,77),(360,65),(420,65)]
            for a,b in zip(pts,pts[1:]): c.line(a[0],a[1],b[0],b[1])
            txt(70,102,'Cladding n₂',8); txt(70,18,'Core n₁ (n₁ > n₂)',8); txt(365,102,'Protective jacket',8)
            txt(230,42,'Zig-zag ray: total internal reflection',8)
        elif self.kind=='acceptance':
            c.setStrokeColor(colors.HexColor('#263746'))
            c.rect(240,35,190,55)
            c.line(240,35,240,90); txt(335,20,'Core',8)
            c.line(20,62,240,62); txt(100,48,'Fibre axis',8)
            arrow(35,105,240,62); arrow(240,62,420,35)
            c.arc(20,62,92,134,startAng=0,extent=-32)
            txt(62,91,'θₐ',10)
            txt(105,119,'Accepted limiting ray',8)
        elif self.kind=='hologram':
            c.rect(30,55,62,35); txt(61,69,'Laser')
            arrow(92,72,140,72); c.circle(150,72,10); txt(150,52,'Beam splitter',7)
            arrow(160,77,225,105); arrow(160,67,225,40)
            c.rect(240,90,65,28); txt(272,103,'Object',8)
            c.rect(350,35,8,80); txt(372,22,'Plate',8)
            arrow(305,104,350,90); arrow(225,40,350,55)
            txt(300,126,'Object beam + reference beam interfere',8)
        elif self.kind=='communication':
            labels=[('Transmitter',25),('Optical fibre',175),('Photodetector / receiver',325)]
            for lab,x in labels:
                c.roundRect(x,48,120,36,5); txt(x+60,63,lab,8)
            arrow(145,66,175,66); arrow(295,66,325,66)
            txt(84,31,'Electrical → optical',7); txt(385,31,'Optical → electrical',7)
        elif self.kind=='levels':
            c.line(55,25,180,25); txt(115,12,'Ground state')
            c.line(55,95,180,95); txt(115,103,'Pump bands')
            c.line(55,65,180,65); txt(115,72,'Metastable level')
            arrow(75,28,75,90); arrow(125,92,125,69); arrow(155,62,155,29)
            txt(315,72,'Pumping raises atoms',9); txt(315,54,'Metastable state stores them',8); txt(315,36,'Laser transition emits photon',8)
        elif self.kind=='profiles':
            # axes and profiles
            c.line(30,25,30,110); c.line(30,25,215,25); txt(20,108,'n',8); txt(120,10,'Radius r',8)
            c.line(40,82,145,82); c.line(145,82,145,45); c.line(145,45,205,45)
            txt(105,92,'Step-index',8)
            c.line(245,25,245,110); c.line(245,25,455,25)
            pts=[(255,95),(280,92),(305,82),(330,67),(355,53),(380,44),(405,40),(445,40)]
            for a,b in zip(pts,pts[1:]): c.line(a[0],a[1],b[0],b[1])
            txt(350,105,'Graded-index',8)
        elif self.kind=='attenuation':
            txt(235,90,'Input power Pᵢₙ',9); arrow(50,75,420,75); txt(235,54,'Optical power decreases along fibre',8)
            txt(235,30,'Loss (dB) = −10 log₁₀(Pout / Pin)',9)

def bullets(items):
    for x in items:
        story.append(Paragraph('• '+x, styles['Bodyx']))
def heading(t): story.append(P(t,'H1x'))
def formula(t): story.append(P(t,'Formula'))
def newpage(): story.append(PageBreak())

story += [Spacer(1,3.1*cm), P('APPLIED PHYSICS — UNIT 4','CoverTitle'),
          P('QUANTUM OPTICS, LASERS, HOLOGRAPHY & OPTICAL FIBRES','CoverTitle'),
          Spacer(1,.4*cm), P('Exam-ready answers for 7-mark and 11-mark questions','CoverSub'),
          Spacer(1,.6*cm), P('Prepared from the uploaded Unit 4 PowerPoint. Includes the questions listed on its final slide, step-by-step derivations, labelled schematic diagrams, comparison tables and a formula revision sheet.','CoverSub'),
          Spacer(1,2*cm), P('How to use this PDF','H2x'),
          P('For a 7-mark answer: write the definition/principle, 4–6 key points, the required equation and a neat labelled diagram where relevant. For an 11-mark answer: add the full working/derivation, explain each step, and finish with applications or significance. Diagrams here are revision schematics; redraw them neatly in your exam.','Bodyx'),
          Spacer(1,1*cm), P('Source note: topics and conventions follow the uploaded PPT. Nd:YAG, CO₂ laser and holography are described at the syllabus level used in the slides.','Smallx'), PageBreak()]

# Q1
heading('Q1. Explain coherence, spontaneous emission and stimulated emission (7 marks)')
story.append(P('Coherence','H2x'))
P1='Coherence is the maintenance of a definite phase relationship between light waves. It is important for stable interference and laser action.'
bullets([P1,'Temporal coherence: phase relationship at the same point over time. It is related to spectral width and coherence time; a narrower spectral line generally means a longer coherence time.','Spatial coherence: phase relationship between different points on the same wavefront. It helps produce clear interference fringes across a beam.'])
story.append(P('Spontaneous emission','H2x'))
bullets(['An atom in an excited energy level returns to a lower level without an external photon triggering the process.','The emitted photon has energy hν = E₂ − E₁. Its phase and direction are random.'])
story.append(P('Stimulated emission','H2x'))
bullets(['An incoming photon of the correct energy interacts with an excited atom and triggers it to emit a second photon.','The emitted photon matches the incoming photon in frequency, phase, direction and polarisation.','This produces amplification of light and is the basic mechanism of laser operation.'])
story.append(Schematic('energy',height=125))
formula('Photon energy:  hν = E₂ − E₁')
story.append(P('Exam conclusion: stimulated emission creates matching photons, while coherence describes a stable phase relationship. Together with population inversion and optical feedback, these enable laser output.','Bodyx'))
newpage()

heading('Q2. Derive Einstein coefficient relations and explain their significance (11 marks)')
story.append(P('Definitions and rate equations','H2x'))
bullets(['B₁₂: coefficient of stimulated absorption from E₁ to E₂.','A₂₁: coefficient of spontaneous emission from E₂ to E₁.','B₂₁: coefficient of stimulated emission from E₂ to E₁.','N₁ and N₂ are populations per unit volume; ρ(ν) is the radiation energy density at frequency ν.'])
formula('Rabs = N₁B₁₂ρ(ν)    |    Rsp = N₂A₂₁    |    Rst = N₂B₂₁ρ(ν)')
story.append(P('Derivation','H2x'))
bullets(['At thermal equilibrium, the upward absorption rate equals the total downward emission rate:'])
formula('N₁B₁₂ρ(ν) = N₂A₂₁ + N₂B₂₁ρ(ν)')
bullets(['Rearrange by collecting the terms containing ρ(ν):'])
formula('ρ(ν) [N₁B₁₂ − N₂B₂₁] = N₂A₂₁')
bullets(['Divide by the bracket and by N₂ to obtain:'])
formula('ρ(ν) = A₂₁ / [(N₁/N₂)B₁₂ − B₂₁]')
bullets(['For equal degeneracy, the Boltzmann population ratio is N₂/N₁ = exp[−hν/(kT)]. Substitute this ratio into the expression for ρ(ν).','Compare the result with Planck’s blackbody radiation law. Matching corresponding terms gives the Einstein relations below.'])
formula('B₁₂ = B₂₁  (equal degeneracy); more generally g₁B₁₂ = g₂B₂₁')
formula('A₂₁ / B₂₁ = 8πhν³ / c³')
story.append(P('Symbols: g₁ and g₂ are degeneracies of the two levels, h is Planck’s constant, ν is transition frequency, c is speed of light, k is Boltzmann’s constant and T is absolute temperature.','Bodyx'))
story.append(P('Significance','H2x'))
bullets(['The absorption and stimulated-emission coefficients are equal for equal degeneracy.','The spontaneous-to-stimulated emission ratio depends strongly on frequency (ν³).','Stimulated emission is the useful process for laser amplification; the equations connect atomic transition probabilities with thermal radiation.'])
story.append(P('Important: these are the standard relations in the spectral-energy-density convention used by the PPT.','Smallx'))
newpage()

heading('Q3. Explain metastable state, pumping, population inversion and threshold condition (7/11 marks)')
story.append(P('Metastable state','H2x'))
bullets(['An excited energy state with a comparatively long lifetime. Atoms stay there longer than in ordinary excited states, allowing them to accumulate.'])
story.append(P('Pumping','H2x'))
bullets(['Pumping is the supply of external energy to raise atoms into excited states.','Optical pumping: light from a flash lamp, as in a Ruby laser. Electrical discharge: used in a He–Ne laser.'])
story.append(P('Population inversion','H2x'))
bullets(['Population inversion occurs when the number of atoms in the upper laser level exceeds that in the lower laser level for the laser transition.','At thermal equilibrium, lower energy levels are more populated, so pumping is needed to create inversion.'])
story.append(Schematic('levels',height=125))
story.append(P('Threshold condition','H2x'))
bullets(['The optical resonator has a highly reflecting mirror and a partially transmitting output coupler. Photons travel back and forth through the active medium, causing further stimulated emission.','Threshold is reached when round-trip optical gain exactly compensates round-trip losses. Below threshold, sustained laser oscillation does not occur; above threshold, stable output can develop.'])
formula('R₁R₂ exp[2(g − αᵢ)L] = 1   (threshold condition)')
bullets(['R₁ and R₂: mirror reflectivities; g: gain coefficient; αᵢ: internal loss coefficient; L: cavity length.','The key requirements are population inversion, stimulated emission, optical feedback, and gain at least equal to losses.'])
newpage()

heading('Q4. Draw and explain Ruby, He–Ne and semiconductor diode lasers (11 marks)')
story.append(P('A. Ruby laser','H2x'))
bullets(['Construction: the active medium is synthetic ruby, Al₂O₃ doped with about 0.05% Cr₂O₃ by weight as stated in the PPT. A xenon flash lamp surrounds the ruby rod. One cavity end is highly reflecting and the other partially transmitting.','Working: optical pumping excites Cr³⁺ ions from the ground state to higher bands. Rapid non-radiative transitions populate a metastable level. Population inversion forms between this level and the ground state; stimulated emission is amplified in the resonator.','Output: red light near 694.3 nm. Ruby is a three-level solid-state laser and commonly operates in pulses.'])
story.append(Schematic('ruby',height=125))
story.append(Schematic('levels',height=115))
story.append(P('B. He–Ne laser','H2x'))
bullets(['Construction: a discharge tube contains helium and neon gas; the PPT gives a mixture around 10:1. Electrodes provide electrical discharge. The optical cavity uses a fully reflecting mirror and a partially transmitting mirror.','Working: electrical discharge excites helium atoms. Collisions transfer energy from helium to neon, producing population inversion in neon. Stimulated emission is amplified between the mirrors.','Output and uses: red light at 632.8 nm, usually continuous-wave; used for alignment, laboratory optics, interferometry, measurement and holography.'])
story.append(Schematic('hene',height=115))
story.append(P('C. Semiconductor diode laser','H2x'))
bullets(['A specially fabricated forward-biased p–n junction emits coherent light. GaAs is a direct-band-gap material named in the PPT.','Electrons and holes recombine in the junction and release photons. The photon energy is related to the band gap.'])
formula('E_g = hν = hc/λ     and     λ (nm) ≈ 1240 / E_g (eV)')
bullets(['Advantages: compact, portable and suitable for optical-fibre communication. Applications include fibre links, optical storage, barcode reading, sensing and laser pointers.'])
newpage()

heading('Q5. Explain Nd:YAG and CO₂ lasers; compare important laser types (7 marks)')
story.append(P('Nd:YAG laser','H2x'))
bullets(['Active medium: yttrium aluminium garnet (YAG) crystal doped with Nd³⁺ ions.','It is a solid-state laser, commonly treated as a four-level system. Optical pumping is provided by a flash lamp or laser diode, depending on design.','Fundamental output is infrared near 1.064 μm. Applications include cutting, drilling, welding, range finding, medical procedures and frequency conversion.'])
story.append(P('CO₂ laser','H2x'))
bullets(['A gas laser with a mixture containing carbon dioxide, nitrogen and helium.','Electrical discharge excites nitrogen; collisions transfer energy to vibrational states of CO₂. Helium helps remove heat and depopulate lower laser levels.','Common output is infrared near 10.6 μm. High-power systems are used for material processing.'])
story.append(P('Comparison table','H2x'))
data=[
['Laser','Medium / pumping','Output / operation','Typical uses'],
['Ruby','Cr³⁺:Al₂O₃; optical pumping','Red, 694.3 nm; pulsed; 3-level','Pulsed laser applications'],
['He–Ne','He–Ne gas; electrical discharge','Red, 632.8 nm; continuous-wave','Alignment, lab optics, holography'],
['Nd:YAG','Nd³⁺ in YAG; optical pumping','IR, 1.064 μm; solid-state','Cutting, welding, medical'],
['CO₂','CO₂/N₂/He gas; discharge','IR, 10.6 μm','Material processing'],
['Diode','Forward-biased direct-gap junction','λ depends on band gap','Fibre links, storage, sensors']
]
t=Table(data, colWidths=[2.2*cm,4.2*cm,4.2*cm,5.1*cm], repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#16324F')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),7.5),('LEADING',(0,0),(-1,-1),9),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#AAB7C4')),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F2F6F8')]),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
story.append(t)
newpage()

heading('Q6. Compare holography and photography; explain recording and reconstruction (11 marks)')
story.append(P('Principle of holography','H2x'))
bullets(['Holography records the interference pattern formed by light scattered from an object and a coherent reference beam.','The interference fringes encode phase-related information as well as intensity. When illuminated appropriately, the recorded pattern diffracts light and reconstructs a wavefront similar to the original object wave.','A laser is normally used because coherent light is needed to create stable interference.'])
story.append(P('Recording process','H2x'))
bullets(['A laser beam is split into two beams by a beam splitter.','The object beam illuminates the object; light scattered from the object reaches the recording plate.','The reference beam reaches the same plate directly. The two beams interfere and form fine fringes. The recorded fringe pattern is the hologram.'])
story.append(Schematic('hologram',height=145))
story.append(P('Reconstruction process','H2x'))
bullets(['The developed hologram is illuminated by a suitable reference beam.','The recorded fringes diffract the light and recreate the object wavefront. The viewer perceives a three-dimensional image with depth/parallax cues.'])
story.append(P('Holography vs photography','H2x'))
data=[['Photography','Holography'],['Records image intensity using a lens.','Records object/reference-beam interference fringes.'],['Can use ordinary light.','Normally needs coherent laser light.'],['Usually gives a two-dimensional image.','Reconstructs a wavefront, giving depth and parallax cues.'],['Does not fully reconstruct phase/wavefront.','A small part of a hologram may retain information about the whole scene.']]
t=Table(data,colWidths=[7.6*cm,7.6*cm])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#245B78')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),8.5),('LEADING',(0,0),(-1,-1),11),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#AAB7C4')),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F2F6F8')]),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
story.append(t)
newpage()

heading('Q7. Derive numerical aperture and acceptance angle; explain optical fibre construction, types, attenuation and applications (11 marks)')
story.append(P('Construction and principle','H2x'))
bullets(['An optical fibre is a thin transparent dielectric waveguide, usually glass or plastic. The core has refractive index n₁ and the surrounding cladding has refractive index n₂, where n₁ > n₂. Protective layers may include silicon coating, buffer jacket, strength members such as Kevlar and an outer jacket.','Guiding occurs by repeated total internal reflection at the core–cladding boundary. The ray must travel from higher index to lower index and strike the boundary at an angle greater than the critical angle.'])
story.append(Schematic('fibre',height=125))
formula('sin θc = n₂ / n₁')
story.append(P('Derivation of numerical aperture (NA)','H2x'))
bullets(['Let n₀ be the refractive index outside the fibre, n₁ the core index and n₂ the cladding index. At the limiting ray, the incidence at the core–cladding boundary equals the critical condition.','At the core–cladding interface, Snell’s law gives:'])
formula('n₁ sin θc = n₂     ⇒     sin θc = n₂ / n₁')
bullets(['From the limiting-ray geometry, the refracted angle inside the core is related to θc. Applying Snell’s law at the fibre entrance:'])
formula('n₀ sin θₐ = n₁ sin r')
bullets(['For the limiting ray, r = 90° − θc, hence sin r = cos θc. Therefore:'])
formula('n₀ sin θₐ = n₁ cos θc')
bullets(['Using cos² θc = 1 − sin² θc and sin θc = n₂/n₁:'])
formula('n₀ sin θₐ = n₁ √(1 − n₂²/n₁²) = √(n₁² − n₂²)')
formula('NA = n₀ sin θₐ = √(n₁² − n₂²)')
bullets(['Numerical aperture measures the light-gathering ability of the fibre. In air, n₀ ≈ 1, so NA = sin θₐ. The acceptance angle θₐ is the maximum launch angle measured from the fibre axis; rotating this angle around the axis forms the acceptance cone.'])
story.append(Schematic('acceptance',height=130))
story.append(P('Fractional refractive-index change','H2x'))
formula('Δ = (n₁ − n₂) / n₁   (common definition used in the PPT)')
story.append(P('Types of fibre','H2x'))
bullets(['By index profile: step-index has a uniform core index with an abrupt change at the cladding; graded-index decreases gradually from the centre toward the cladding.','By propagation mode: single-mode carries one mode, has a small core and low modal dispersion; multimode carries many modes, has a larger core and is easier to couple light into but has greater modal dispersion.','By material: all-glass, all-plastic, glass core with plastic cladding, and polymer-clad silica (PCS).'])
story.append(Schematic('profiles',height=130))
story.append(P('Attenuation','H2x'))
bullets(['Attenuation is the reduction in optical power as light travels through a fibre. Causes include Rayleigh scattering, absorption, bending and connector/splice losses. Loss is often expressed in dB or dB/km.'])
formula('Loss (dB) = −10 log₁₀(Pout / Pin)')
story.append(Schematic('attenuation',height=95))
story.append(P('Communication system and applications','H2x'))
bullets(['Basic blocks: transmitter/light source (LED or diode laser) → optical fibre channel → photodetector/receiver → amplifier or signal restorer.','Applications: optical communication, fibre-optic sensors and medical endoscopy. Advantages: high information capacity, low weight, small size, electrical isolation and low susceptibility to interference/crosstalk.'])
story.append(Schematic('communication',height=115))
newpage()

heading('Extra diagrams to practise for 7/11-mark answers')
story.append(P('Use these schematics as drawing guides. In the exam, use a pencil and ruler, keep labels outside the drawing where possible, and add the key formula beside the diagram.','Bodyx'))
for title,kind,desc in [
('1. Laser resonator','laser','Label pump source, active medium, fully reflecting mirror, output coupler and laser output.'),
('2. Energy transitions','energy','Show absorption upward and emission downward between E₁ and E₂. Write hν = E₂ − E₁.'),
('3. Ruby laser','ruby','Label ruby rod, xenon flash lamp, cavity mirrors and red output at approximately 694.3 nm.'),
('4. He–Ne laser','hene','Label discharge tube, He–Ne gas, electrodes, mirrors and 632.8 nm output.'),
('5. Hologram recording','hologram','Show laser, beam splitter, object beam, reference beam and recording plate.'),
('6. Optical fibre ray path','fibre','Label core n₁, cladding n₂, protective jacket and zig-zag ray.'),
('7. Acceptance angle','acceptance','Show fibre axis, limiting ray and θₐ measured from the axis.'),
('8. Step-index vs graded-index profiles','profiles','Show abrupt index change for step-index and smooth decrease for graded-index.'),
('9. Optical communication system','communication','Label transmitter, fibre channel and photodetector/receiver.')]:
    story.append(P(title,'H2x')); story.append(Schematic(kind,height=115)); story.append(P(desc,'Smallx'))
newpage()

heading('Last-minute formula sheet')
for f in [
'Photon transition: hν = E₂ − E₁',
'Semiconductor diode laser: E_g = hν = hc/λ; λ (nm) ≈ 1240 / E_g (eV)',
'Einstein rate equations: Rabs = N₁B₁₂ρ(ν); Rsp = N₂A₂₁; Rst = N₂B₂₁ρ(ν)',
'Einstein relations: g₁B₁₂ = g₂B₂₁; A₂₁/B₂₁ = 8πhν³/c³',
'Laser threshold: R₁R₂ exp[2(g − αᵢ)L] = 1',
'Critical angle: sin θc = n₂/n₁, where n₁ > n₂',
'Numerical aperture: NA = n₀ sin θₐ = √(n₁² − n₂²)',
'Fractional index change: Δ = (n₁ − n₂)/n₁ (common definition)',
'Fibre attenuation: Loss (dB) = −10 log₁₀(Pout/Pin)'
]:
    formula(f)
story.append(P('Quick writing strategy','H2x'))
bullets(['7 marks: definition/principle + 4–6 clear points + equation + diagram if relevant.','11 marks: definition + construction/setup + labelled diagram + stepwise working/derivation + applications/significance.','For derivations, define every symbol and show the intermediate algebraic steps rather than writing only the final formula.','Keep the PPT convention for Δ and Einstein relations consistent with your classroom notes.'])
def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#CBD5DD')); canvas.line(1.6*cm,1.35*cm,A4[0]-1.6*cm,1.35*cm)
    canvas.setFont('Helvetica',8); canvas.setFillColor(colors.HexColor('#607D8B'))
    canvas.drawString(1.6*cm,.9*cm,'Applied Physics • Unit 4 • Exam preparation')
    canvas.drawRightString(A4[0]-1.6*cm,.9*cm,f'Page {doc.page}')
    canvas.restoreState()
doc=SimpleDocTemplate(out,pagesize=A4,rightMargin=1.6*cm,leftMargin=1.6*cm,topMargin=1.55*cm,bottomMargin=1.7*cm,title='Unit 4 Quantum Optics Exam Q&A')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
os.path.getsize(out)