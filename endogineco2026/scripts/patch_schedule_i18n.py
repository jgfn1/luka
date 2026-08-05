#!/usr/bin/env python3
"""Patch EN/ES schedule tbody translations from the updated Portuguese panels."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

DETAIL = "font-weight:400;margin-top:.35rem;font-size:.88rem;line-height:1.45"

EN = {
    "sch.openCongress": f"""
                <tr><td>08:00 - 08:15</td><td colspan="2" class="session-break"><strong>Accreditation</strong></td></tr>
                <tr><td>08:15 -  08:30</td><td>Opening</td><td class="speaker-name">Érica Batista <br />Edilberto Rocha <br />Jardel Soares <br />Iolanda Matias <br />Agostinho Machado <br />Juliana Zaidan</td></tr>""",
    "sch.friAudA": f"""
                <tr><td colspan="3" class="session-header"><strong>08:30 - 09:50<br />(1 hour and<br />20 min)</strong><br />PANEL 1 - Nerve-sparing in Endometriosis Surgery<br />Chair: Fernando Prado - PE<br />Discussants: Renato Barretto - SP, Melissandro Lacerda - PB, Anna Luiza Lobão - PB</td></tr>
                <tr><td>08:30 - 09:00<br />(30 min)</td><td>Do you know where the main pelvic nerves run? Why does it matter in complex Endometriosis surgery?</td><td class="speaker-name">Kathiane Lustosa - CE</td></tr>
                <tr><td>09:00 - 09:20<br />(20 min)</td><td>Main nerve injuries in Endometriosis. What are the main symptoms?</td><td class="speaker-name">Fabio Ohara - SP</td></tr>
                <tr><td>09:20 - 09:40<br />(20 min)</td><td>Should every nerve injury from endometriosis be operated on?</td><td class="speaker-name">Raquel Magalhães - SP</td></tr>
                <tr><td>09:40 - 09:50<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td>09:50 - 10:20<br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:20 - 11:40<br />(1 hour and<br />20 min)</strong><br />PANEL 2 - Video Hysteroscopy<br />Chair: Helena Nagy - PE<br />Discussants: Neidson Menezes - PE, Aurélio Costa - PE, Felipe Rocha - PE</td></tr>
                <tr><td>10:20 - 10:30<br />(10 min)</td><td>Outpatient Video Hysteroscopy: how far can we go? How to minimize fear?<br />How to reduce pain?</td><td class="speaker-name">Mariana Vieira  - SP</td></tr>
                <tr><td>10:30 - 10:45<br />(15 min)</td><td>Endometrial Hyperplasia and Endometrial Cancer. Can it still be managed conservatively? Until when?</td><td class="speaker-name">Jaime Calderon - Mexico <br />*Online*</td></tr>
                <tr><td>10:45 - 11:00<br />(15 min)</td><td>Using Hysteroscopy to treat AUB (abnormal uterine bleeding).<br />Where does it apply? What is the limit?</td><td class="speaker-name">Mariana Roma - PE</td></tr>
                <tr><td>11:00 - 11:15<br />(15 min)</td><td>How to minimize complications in Hysteroscopy and how to handle them if they occur?</td><td class="speaker-name">Ana Carolina Serafim - PE</td></tr>
                <tr><td>11:15 - 11:30<br />(15 min)</td><td>The challenges of retained products of conception — how can Hysteroscopy help?</td><td class="speaker-name">Guilherme Zanluchi -SP</td></tr>
                <tr><td>11:30 - 11:40<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td>11:40 - 12:00<br />(20 min)</td><td>ZYDUS SYMPOSIUM - Iron replacement - A key item for safe surgery</td><td class="speaker-name">Jardel Soares - PE</td></tr>
                <tr><td>12:00 - 13:30<br />(1 hour and<br />30 min)</td><td colspan="2" class="session-break"><strong>FREE BREAK</strong></td></tr>
                <tr><td>13:30 - 15:30<br />(2 hours)</td><td colspan="2" class="session-live"><strong>LIVE SURGERIES</strong><div style="{DETAIL}">Chair: Mauro Aguiar - PE<br />Discussants: Kelwin Madson - PE , Neidson Menezes PE , Phabllo Rodrigo - PE</div><div style="{DETAIL}">* Hospital Santa Joana Recife - PE <br />Kathyane Lustosa CE <br />Case lead:  Maria Cecília Siqueira - PE <br /> <br />* Hospital Barão de Lucena - PE<br />Patrick Bellelis - SP  <br />Mariana Vieira  - SP<br />Case lead: Carolina Feitosa - PE <br /><br />* Hospital das Nações CWB  <br />Mônica Zomer PR -  ROOM 1 <br />William Kondo PR - ROOM 2 <br /><br />* Hospital Campinas - SP<br />Carlos Godoy - SP</div></td></tr>
                <tr><td>15:30 - 16:00<br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>16:00 - 16:50<br />(50 min)</strong><br />PANEL 3 - Uterine Fibroids<br />Chair: Mariana Santiago - PE <br />Discussants: Jessica Cesario - PE, Rafael Alves - PE, Alisson Chianca - MA, Lilia Mendes - CE</td></tr>
                <tr><td>16:00 - 16:10<br />(10 min)</td><td>Strategies to reduce bleeding in myomectomies — what is my strategy?</td><td class="speaker-name">Melissandro Lacerda - PB</td></tr>
                <tr><td>16:10 - 16:20<br />(10 min)</td><td>Fibroid extraction — is there a best technique?</td><td class="speaker-name">Mauro Aguiar - PE</td></tr>
                <tr><td>16:20 - 16:30<br />(10 min)</td><td>Surgical conversion in myomectomy — failure of indication or the right decision?</td><td class="speaker-name">Anna Luiza Lobão - PB</td></tr>
                <tr><td>16:30 - 16:40<br />(10 min)</td><td>Myomectomy — which incision, suture and thread for a refined, fast and bloodless surgery?</td><td class="speaker-name">Andreisa Bilhar - CE</td></tr>
                <tr><td>16:40 - 16:50<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>16:50 - 17:20<br />(30 min)</strong><br />Lectures<br />Chair: Dr. Edilberto Rocha - PE</td></tr>
                <tr><td>16:50 - 17:05 <br />(15 min)</td><td>How can AI influence your practice from the office to post-op?<br />Chair: Edilberto Rocha - PE</td><td class="speaker-name">Jardel Soares - PE</td></tr>
                <tr><td>17:05 - 17:20<br />(15 min)</td><td>Complications in minimally invasive surgery — how should I manage them?</td><td class="speaker-name">Giuliano Borrelli - SP</td></tr>
                <tr><td>17:25 - 18:10<br />(45 min)</td><td>TALK SHOW - &quot;The endometriosis patient's journey&quot;<br />How to build a successful practice<br />Coordinator: Mariana Muniz - PE</td><td class="speaker-name">Rosaura Almeida - PE (nutritionist)<br />Isaura Vieira - PE (acupuncturist)<br />Arthur Farias -PB (urologist)<br />Kathyane Lustosa - CE, (gynecologist)<br />Mayara Macedo -PE, (pelvic physiotherapist)<br />Macira Sotero- PE, (psychologist)</td></tr>
                <tr><td>18:10</td><td colspan="2" class="session-break"><strong>Closing</strong></td></tr>""",
    "sch.friAudB": f"""
                <tr><td colspan="3" class="session-header"><strong>08:30 - 10:10<br />(1 hour and 40 min)</strong><br />VIDEO SHOWCASES - Semi-edited videos</td></tr>
                <tr><td>08:30 - 08:50<br />(20 min)</td><td>How the use of fluorescence helped me in this case</td><td class="speaker-name">Guilherme Zanluchi - SP</td></tr>
                <tr><td>08:50 - 09:10<br />(20 min)</td><td>I had to change my strategy in treating this bowel disease</td><td class="speaker-name">Claudia Joaquim - RJ</td></tr>
                <tr><td>09:10 - 09:30<br />(20 min)</td><td>My strategy for this difficult myomectomy</td><td class="speaker-name">Alisson Chianca - MA</td></tr>
                <tr><td>09:30 - 09:50<br />(20 min)</td><td>Robotic Cerclage. When? Tips and tricks?</td><td class="speaker-name">Patrick Bellelis - SP</td></tr>
                <tr><td>09:50 - 10:10<br />(20  min)</td><td>Isthmocele — treat via laparoscopy, robotics or hysteroscopy?</td><td class="speaker-name">Mariana Vieira - SP</td></tr>
                <tr><td>10:10 - 10:40 <br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:40 - 11:50<br />(1 hour and<br />10 min)</strong><br />PANEL 1 - Imaging<br />Chair: Taciana Morais - PE<br />Discussants: Marina Almeida - DF</td></tr>
                <tr><td>10:40 - 11:10<br />(30 min)</td><td>CROSS FIRE - Present your strengths</td><td></td></tr>
                <tr><td></td><td>What can't be missing in endometriosis mapping ultrasound?<br />What has technology improved?</td><td class="speaker-name">Penélope Melo - PE</td></tr>
                <tr><td></td><td>What can't be missing in MRI for endometriosis screening?</td><td class="speaker-name">Pedro Guedes - PE</td></tr>
                <tr><td>11:10 - 11:25<br />(15 min)</td><td>How has 3D reconstruction come to support the surgeon? I'll show you in practice</td><td class="speaker-name">Italo Cruz - PE</td></tr>
                <tr><td>11:25 - 11:40<br />(15 min)</td><td>Will AI replace humans in the radiological diagnosis of endometriosis?</td><td class="speaker-name">Nadja Rolim - PE</td></tr>
                <tr><td>11:40 - 11:50<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td>11:50 - 13:30<br />(1 hour and 40 min)</td><td colspan="2" class="session-break"><strong>FREE BREAK</strong></td></tr>
                <tr><td>13:30 - 15:30<br />(2 hours)</td><td colspan="2" class="session-live"><strong>LIVE SURGERIES - IN ROOM A</strong></td></tr>
                <tr><td>15:30 - 16:00<br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td>16:00 - 16:15<br />(15 min)</td><td>BAYER SYMPOSIUM - Medical treatment of Endometriosis according to the ACOH 2026 protocol</td><td class="speaker-name">Jardel Soares - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>16:15 - 17:55<br />(1 hour and<br />40 min)</strong><br />PANEL 2 - In my office<br />Chair: Simone Carvalho - PE <br />Discussants: Leonardo Lima - PE, Érica</td></tr>
                <tr><td>16:15 - 16:35 <br />(20 min)</td><td>Climacteric and Menopause in the patient with Endometriosis. How do I manage case by case?</td><td class="speaker-name">Priscilla Vieira - PE</td></tr>
                <tr><td>16:35 - 16:55<br />(20 min)</td><td>Diagnostic methods for endometriosis — what do we have? What are the new perspectives?</td><td class="speaker-name">Cicilia Pontes - PE</td></tr>
                <tr><td>16:55 - 17:15 <br />(20 min)</td><td>Endometriosis in adolescence: how do I manage it? How to avoid excessive surgeries?</td><td class="speaker-name">Lilia Mendes - CE</td></tr>
                <tr><td>17:15 - 17:35<br />(20 min)</td><td>Painful intercourse, vaginismus and relationship difficulties as sequelae of endometriosis. How to manage?</td><td class="speaker-name">Aleide Tavares - PE</td></tr>
                <tr><td>17:35 - 17:45<br />(10  min)</td><td>Negative impacts of endometriosis on society. How can we reverse this?</td><td class="speaker-name">Iolanda Matias - PE</td></tr>
                <tr><td>17:45 - 17:55<br />(10  min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td>17:55 - 18:40<br />(45 min)</td><td>YOU DECIDE!<br />Making decisions in surgical treatment in gynecology<br />Coordination: Iolanda Matias - PE</td><td></td></tr>
                <tr><td></td><td>Clinical Case 1 - Severe endometriosis with renal exclusion</td><td class="speaker-name">Andréa Perez - SP</td></tr>
                <tr><td></td><td>Clinical Case 2 - PROLAPSE + URINARY INCONTINENCE</td><td class="speaker-name">Sara Arcanjo - CE</td></tr>
                <tr><td></td><td>Clinical Case 3 - ADENOMYOSIS</td><td class="speaker-name">Raquel Magalhães - SP</td></tr>
                <tr><td>18:40</td><td colspan="2" class="session-break"><strong>Closing</strong></td></tr>""",
    "sch.satAudA": f"""
                <tr><td>08:00 - 10:00            (2 hours)</td><td colspan="2" class="session-live"><strong>LIVE SURGERIES                                                                                                                                                                           Chair: Iolanda Matias - PE</strong><div style="{DETAIL}">Discussants:  Mariana Roma - PE, Felipe Rocha - PE, Guilherme Zanluchi - SP, Felipe Rocha - PB</div><div style="{DETAIL}">* Hospital Santa Joana Recife  - PE<br />Raquel Magalhães SP<br />Case lead: Sidraiton Melo - PE <br /><br />* Hospital Barão de Lucena  - PE<br />Sara Arcanjo - CE <br />Andreisa Bilhar - CE <br />Case lead: Eveline Martins Sampaio - PE <br /><br />* Hospital  Bragança Paulista <br />Dr. Rodrigo Sader Heck SP<br /><br />* Hospital Itaim Bibi - SP <br />Dr Paulo Ayroza /<br />Helizabeth Salomão</div></td></tr>
                <tr><td>10:00 - 10:30 <br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:30<br />(1 hour and<br />10 min)</strong><br />PANEL 1 - Infertility and Endometriosis <br />Chair:<br />Discussants:</td></tr>
                <tr><td>10:30 - 10:45<br />(15 min)</td><td>What to do first in the patient with endometriosis: IVF before and then operate, or operate and then IVF?</td><td class="speaker-name">Patrick Bellelis - SP<br />*Online*</td></tr>
                <tr><td>10:45 - 11:00<br />(15 min)</td><td>In the hysteroscopic workup of the infertile woman: what should I look for? How to treat?</td><td class="speaker-name">Altina Castelo Branco - PE</td></tr>
                <tr><td>11:00 - 11:15<br />(15 min)</td><td>The challenge of managing uterine malformations: from diagnosis to choosing the ideal approach. What is the best surgical strategy?</td><td class="speaker-name">Mariana Vieira - SP<br />*Online*</td></tr>
                <tr><td>11:15 - 11:30<br />(15 min)</td><td>From implantation to delivery — does anything change in the follow-up of women with endometriosis and infertility?</td><td class="speaker-name">Edilberto Rocha - PE</td></tr>
                <tr><td>11:30 - 11:40 <br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>11:40 - 12:35<br />(55 min)</strong><br />Lectures<br /> Chair: Walter Ivo Paiva PE</td></tr>
                <tr><td>11:40 - 12:00<br />(20 min)</td><td>Lecture: Robotic Surgery in Gynecology and other associated technologies —<br />What benefits have we already proven?</td><td class="speaker-name">Jordanna Diniz - DF<br />*Online*</td></tr>
                <tr><td>12:00 - 12:20<br />(20 min)</td><td>Lecture: ERAS Protocol - Does it apply even in highly complex surgeries?</td><td class="speaker-name">Carlos Godoy - SP</td></tr>
                <tr><td>12:20 - 12:35<br />(15 min)</td><td>Lecture: Clinical pain management - What's new? Cannabis?<br />And what's new in advanced pain management?</td><td class="speaker-name">Luiz Severo - PE</td></tr>
                <tr><td>12:35 - 12:55<br />(20 min)</td><td>ABIOCON SYMPOSIUM</td><td class="speaker-name">Fernando Prado - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>12:55 - 13:35<br />(40 min)</strong><br />Lectures<br /> Chair: Jardel Soares - PE</td></tr>
                <tr><td>12:55 - 13:15<br />(20 min)</td><td>Life lessons: The survival of the laparoscopic and robotic surgeon — from ergonomics to mental health</td><td class="speaker-name">Fernando Heredia - Chile <br />*Online*</td></tr>
                <tr><td>13:15 - 13:35<br />(20 min)</td><td>Life lessons: Deciding is harder than operating</td><td class="speaker-name">Ana Sierra - Mexico <br />*Online*</td></tr>
                <tr><td colspan="3" class="session-header"><strong>13:35 - 14:25            (50 min)</strong><br />PANEL 2 - Coloproctology panel<br />Chair: Marcos Saturnino - PE<br />Discussants: Gilberto Pagnissin - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>13:35 - 14:05            (30 min)</strong><br />TRIPLE CROSS FIRE — the TRIELO</td></tr>
                <tr><td></td><td>Shaving</td><td class="speaker-name">Paulo Mozart - PE</td></tr>
                <tr><td></td><td>Discoid and double discoid</td><td class="speaker-name">Claudia Joaquim - RJ</td></tr>
                <tr><td></td><td>Segmental resection</td><td class="speaker-name">Renato Barretto - SP</td></tr>
                <tr><td>14:05 - 14:15            (10 min)</td><td>Intestinal dehiscences — how to manage?</td><td class="speaker-name">Cláudia Joaquim - RJ</td></tr>
                <tr><td>14:15 - 14:25            (10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td>14:25 - 14:35<br />(10 min)</td><td colspan="2" class="session-break"><strong>BREAK</strong></td></tr>
                <tr><td>14:35 - 16:15<br />(1 hour and 40 min)</td><td colspan="2" class="session-live"><strong>LIVE SURGERIES                                                                                                                                                                                        Coordinator: Jardel Soares - PE</strong><div style="{DETAIL}">Discussants: Sidraiton Melo - PE, Andreisa Bilhar - CE, Yole Minervino - PB</div><div style="{DETAIL}">* Hospital Santa Joana Recife - PE<br />Giuliano Borrelli - SP<br />Case lead: <br /><br />* Hospital Barão de Lucena - PE<br />Fabio Ohara - SP <br />Case lead:<br /><br />*Cúcuta - Colombia  <br />Santiago Machicado <br /><br />* CUSCO - Peru<br />Eric Arancibia<br /><br />*Hospital Mocelia - Mexico <br />Armando Menocau</div></td></tr>
                <tr><td>16:15</td><td colspan="2" class="session-break"><strong>Closing</strong></td></tr>
                <tr><td>16:30</td><td colspan="2" class="session-break"><strong>Feijoada (optional)</strong></td></tr>""",
    "sch.satAudB": f"""
                <tr><td>08:00 - 10:00</td><td colspan="2" class="session-live"><strong>LIVE SURGERIES - ROOM A</strong></td></tr>
                <tr><td>10:00 - 10:30 <br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:30  - 11:10<br />(40 min)</strong><br />Lectures - Urology in action<br />Chair: Guilherme Lima - PE<br />Discussants: Evandilson Guenes - PE, Rafael Oliveira - PE</td></tr>
                <tr><td>10:30 - 10:45<br />(15 min)</td><td>Treatment of ureteral endometriosis — in frozen pelvis, is there a best technique?<br />Is there superiority in the approach route?</td><td class="speaker-name">Antônio César Cruz - PE</td></tr>
                <tr><td>10:45 - 11:00<br />(15 min)</td><td>Bladder injury — limits of resection. Are there long-term repercussions?</td><td class="speaker-name">Arthur Farias - PB</td></tr>
                <tr><td>11:00 -11:10              <br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>11:10 - 11:40<br />(30 min)</strong><br />Lectures<br />Chair: Diogenes Fontão - PE</td></tr>
                <tr><td>11:10 - 11:25 <br />(15 min)</td><td>Lecture: When pelvic pain is much more than endometriosis</td><td class="speaker-name">Giuliano Borrelli - SP</td></tr>
                <tr><td>11:25 - 11:40            (15 min)</td><td>Lecture: PBM (Patient Blood Management) — How to prepare the patient for surgery? How long to tolerate anemia? How to optimize your surgical outcomes?</td><td class="speaker-name">Dahra Teles - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>11:40 - 12:30<br />(50 min)</strong><br />PANEL 1 - Multidisciplinarity<br />Chair: Juliana  Zaidan - PE<br />Discussants: Natália  Fernandes - PE, Rita Santos - PE, Leonardo Lima - PE, Sirley Portela - PE</td></tr>
                <tr><td>11:40 - 11:50<br />(10 min)</td><td>The best diet for the endometriosis patient? Is there room for supplements?</td><td class="speaker-name">Nara Parente - CE</td></tr>
                <tr><td>11:50 - 12:00<br />(10 min)</td><td>Pelvic physiotherapy before and after surgery. What proven results do we have?</td><td class="speaker-name">Isabella Frota - CE</td></tr>
                <tr><td>12:00 - 12:10<br />(10 min)</td><td>Acupuncture as an adjuvant treatment in gynecologic conditions.</td><td class="speaker-name">Isaura Vieira  - PE</td></tr>
                <tr><td>12:10 - 12:20<br />(10 min)</td><td>The impacts of physical activity on endometriosis treatment.<br />What is the best exercise?</td><td class="speaker-name">Paulo Carvalho - PE</td></tr>
                <tr><td>12:20 - 12:30<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td>12:35 - 12:55<br />(20 min)</td><td>ABIOCON SYMPOSIUM - (ROOM A)</td><td></td></tr>
                <tr><td>12:55 - 13:40<br />(45 min)</td><td colspan="2" class="session-break"><strong>FREE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>13:40 - 14:20<br />(40 min)</strong><br />Urogynecology in Focus<br />Chair: Eveline Martins Sampaio - PE<br />Discussants: Sônia Lavínia - PE, Vanessa Freitas - PE, Arthur Rangel - PE, Guilherme Zanluchi - SP</td></tr>
                <tr><td>13:40 - 13:50<br />(10 min)</td><td>Urodynamic study — when to order? How to interpret?</td><td class="speaker-name">Mônica Diniz - PE</td></tr>
                <tr><td>13:50 - 14:00<br />(10 min)</td><td>Treatment of genital prolapse — which technique is best? And the results? I'll show you in practice</td><td class="speaker-name">Sara Arcanjo - CE</td></tr>
                <tr><td>14:00 - 14:10<br />(10 min)</td><td>Urinary incontinence — how to manage? When to operate? I'll show you in practice</td><td class="speaker-name">Andreisa Bilhar  - CE</td></tr>
                <tr><td>14:10 - 14:20<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discussion</strong></td></tr>
                <tr><td>14:20 - 14:35<br />(15 min)</td><td colspan="2" class="session-break"><strong>BREAK</strong></td></tr>
                <tr><td>14:35 - 16:15<br />(1 hour and 40 min)</td><td colspan="2" class="session-live"><strong>LIVE SURGERIES - ROOM A</strong></td></tr>
                <tr><td>16:15</td><td colspan="2" class="session-break"><strong>Closing</strong></td></tr>
                <tr><td>16:30</td><td colspan="2" class="session-break"><strong>Feijoada (optional)</strong></td></tr>""",
}

ES = {
    "sch.openCongress": f"""
                <tr><td>08:00 - 08:15</td><td colspan="2" class="session-break"><strong>Acreditación</strong></td></tr>
                <tr><td>08:15 -  08:30</td><td>Apertura</td><td class="speaker-name">Érica Batista <br />Edilberto Rocha <br />Jardel Soares <br />Iolanda Matias <br />Agostinho Machado <br />Juliana Zaidan</td></tr>""",
    "sch.friAudA": f"""
                <tr><td colspan="3" class="session-header"><strong>08:30 - 09:50<br />(1 hora y<br />20 min)</strong><br />MESA 1 - Nerve-sparing (preservación nerviosa) en la Cirugía de Endometriosis<br />Presidente: Fernando Prado - PE<br />Debatientes: Renato Barretto - SP, Melissandro Lacerda - PB, Anna Luiza Lobão - PB</td></tr>
                <tr><td>08:30 - 09:00<br />(30 min)</td><td>¿Sabe por dónde pasan los principales nervios pélvicos? ¿Cuál es su importancia en la cirugía compleja de Endometriosis?</td><td class="speaker-name">Kathiane Lustosa - CE</td></tr>
                <tr><td>09:00 - 09:20<br />(20 min)</td><td>¿Principales lesiones nerviosas en la Endometriosis? ¿Cuáles son los principales síntomas?</td><td class="speaker-name">Fabio Ohara - SP</td></tr>
                <tr><td>09:20 - 09:40<br />(20 min)</td><td>¿Toda lesión nerviosa por endometriosis debe ser operada?</td><td class="speaker-name">Raquel Magalhães - SP</td></tr>
                <tr><td>09:40 - 09:50<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td>09:50 - 10:20<br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:20 - 11:40<br />(1 hora y<br />20 min)</strong><br />MESA 2 - Video Histeroscopia<br />Presidente: Helena Nagy - PE<br />Debatientes: Neidson Menezes - PE, Aurélio Costa - PE, Felipe Rocha - PE</td></tr>
                <tr><td>10:20 - 10:30<br />(10 min)</td><td>Video Histeroscopia Ambulatoria: ¿hasta dónde llegar? ¿Cómo minimizar el temor?<br />¿Cómo disminuir el dolor?</td><td class="speaker-name">Mariana Vieira  - SP</td></tr>
                <tr><td>10:30 - 10:45<br />(15 min)</td><td>Hiperplasia Endometrial y Cáncer de Endometrio. ¿Aún se puede ser conservador? ¿Hasta cuándo?</td><td class="speaker-name">Jaime Calderon - México <br />*Online*</td></tr>
                <tr><td>10:45 - 11:00<br />(15 min)</td><td>Usando la Histeroscopia para el tratamiento del SUA (sangrado uterino anormal).<br />¿Dónde se aplica? ¿Cuál es el límite?</td><td class="speaker-name">Mariana Roma - PE</td></tr>
                <tr><td>11:00 - 11:15<br />(15 min)</td><td>¿Cómo minimizar las complicaciones en las Histeroscopias y, si ocurren, cómo manejarlas?</td><td class="speaker-name">Ana Carolina Serafim - PE</td></tr>
                <tr><td>11:15 - 11:30<br />(15 min)</td><td>Los desafíos de la retención de restos ovulares — ¿Cómo puede ayudar la Histeroscopia?</td><td class="speaker-name">Guilherme Zanluchi -SP</td></tr>
                <tr><td>11:30 - 11:40<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td>11:40 - 12:00<br />(20 min)</td><td>SIMPOSIO ZYDUS - La reposición de Hierro - Ítem fundamental para una cirugía segura</td><td class="speaker-name">Jardel Soares - PE</td></tr>
                <tr><td>12:00 - 13:30<br />(1 hora y<br />30 min)</td><td colspan="2" class="session-break"><strong>DESCANSO LIBRE</strong></td></tr>
                <tr><td>13:30 - 15:30<br />(2 horas)</td><td colspan="2" class="session-live"><strong>CIRUGÍAS EN VIVO</strong><div style="{DETAIL}">Presidente: Mauro Aguiar - PE<br />Debatientes: Kelwin Madson - PE , Neidson Menezes PE , Phabllo Rodrigo - PE</div><div style="{DETAIL}">* Hospital Santa Joana Recife - PE <br />Kathyane Lustosa CE <br />Conducción del caso:  Maria Cecília Siqueira - PE <br /> <br />* Hospital Barão de Lucena - PE<br />Patrick Bellelis - SP  <br />Mariana Vieira  - SP<br />Conducción del caso: Carolina Feitosa - PE <br /><br />* Hospital das Nações CWB  <br />Mônica Zomer PR -  SALA 1 <br />William Kondo PR - SALA 2 <br /><br />* Hospital Campinas - SP<br />Carlos Godoy - SP</div></td></tr>
                <tr><td>15:30 - 16:00<br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>16:00 - 16:50<br />(50 min)</strong><br />MESA 3 - Miomas Uterinos<br />Presidente: Mariana Santiago - PE <br />Debatientes: Jessica Cesario - PE, Rafael Alves - PE, Alisson Chianca - MA, Lilia Mendes - CE</td></tr>
                <tr><td>16:00 - 16:10<br />(10 min)</td><td>Estrategias para disminuir el sangrado en las miomectomías — ¿cuál es mi estrategia?</td><td class="speaker-name">Melissandro Lacerda - PB</td></tr>
                <tr><td>16:10 - 16:20<br />(10 min)</td><td>Extracción de miomas — ¿existe la mejor técnica?</td><td class="speaker-name">Mauro Aguiar - PE</td></tr>
                <tr><td>16:20 - 16:30<br />(10 min)</td><td>Conversión quirúrgica en miomectomía — ¿falla en la indicación o decisión correcta?</td><td class="speaker-name">Anna Luiza Lobão - PB</td></tr>
                <tr><td>16:30 - 16:40<br />(10 min)</td><td>Miomectomía — ¿cuál es la mejor incisión, el mejor punto y el mejor hilo para una cirugía refinada, rápida y sin sangrado?</td><td class="speaker-name">Andreisa Bilhar - CE</td></tr>
                <tr><td>16:40 - 16:50<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>16:50 - 17:20<br />(30 min)</strong><br />Conferencias<br />Presidente: Dr. Edilberto Rocha - PE</td></tr>
                <tr><td>16:50 - 17:05 <br />(15 min)</td><td>¿Cómo puede la IA influir en su conducta desde el consultorio al postoperatorio?<br />Presidente: Edilberto Rocha - PE</td><td class="speaker-name">Jardel Soares - PE</td></tr>
                <tr><td>17:05 - 17:20<br />(15 min)</td><td>Complicaciones en cirugías mínimamente invasivas — ¿cómo debo conducir?</td><td class="speaker-name">Giuliano Borrelli - SP</td></tr>
                <tr><td>17:25 - 18:10<br />(45 min)</td><td>TALK SHOW - &quot;La jornada de la paciente con endometriosis&quot;<br />Cómo tener un consultorio de éxito<br />Coordinadora: Mariana Muniz - PE</td><td class="speaker-name">Rosaura Almeida - PE (nutricionista)<br />Isaura Vieira - PE (acupunturista)<br />Arthur Farias -PB (urólogo)<br />Kathyane Lustosa - CE, (ginecóloga)<br />Mayara Macedo -PE, (fisioterapeuta pélvica)<br />Macira Sotero- PE, (psicóloga)</td></tr>
                <tr><td>18:10</td><td colspan="2" class="session-break"><strong>Cierre</strong></td></tr>""",
    "sch.friAudB": f"""
                <tr><td colspan="3" class="session-header"><strong>08:30 - 10:10<br />(1 hora y 40 min)</strong><br />VIDEOS SHOW CASES - Videos semi-editados</td></tr>
                <tr><td>08:30 - 08:50<br />(20 min)</td><td>Cómo el uso de la fluorescencia me ayudó en este caso</td><td class="speaker-name">Guilherme Zanluchi - SP</td></tr>
                <tr><td>08:50 - 09:10<br />(20 min)</td><td>Tuve que cambiar mi estrategia en el tratamiento de esa enfermedad intestinal</td><td class="speaker-name">Claudia Joaquim - RJ</td></tr>
                <tr><td>09:10 - 09:30<br />(20 min)</td><td>Mi estrategia para esa miomectomía difícil</td><td class="speaker-name">Alisson Chianca - MA</td></tr>
                <tr><td>09:30 - 09:50<br />(20 min)</td><td>Cerclaje Robótico. ¿Cuándo? ¿Tips y trucos?</td><td class="speaker-name">Patrick Bellelis - SP</td></tr>
                <tr><td>09:50 - 10:10<br />(20  min)</td><td>Istmocele — ¿tratar por vía laparoscópica, robótica o histeroscopia?</td><td class="speaker-name">Mariana Vieira - SP</td></tr>
                <tr><td>10:10 - 10:40 <br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:40 - 11:50<br />(1 hora y<br />10 min)</strong><br />MESA 1 - Imagen<br />Presidente: Taciana Morais - PE<br />Debatientes: Marina Almeida - DF</td></tr>
                <tr><td>10:40 - 11:10<br />(30 min)</td><td>CROSS FIRE - Presente sus superioridades</td><td></td></tr>
                <tr><td></td><td>¿Qué no puede faltar en la ecografía de mapeo de la endometriosis?<br />¿Qué se ha podido mejorar con la tecnología?</td><td class="speaker-name">Penélope Melo - PE</td></tr>
                <tr><td></td><td>¿Qué no puede faltar en la resonancia para el cribado de endometriosis?</td><td class="speaker-name">Pedro Guedes - PE</td></tr>
                <tr><td>11:10 - 11:25<br />(15 min)</td><td>¿Cómo la reconstrucción 3D vino a dar apoyo al cirujano? Te lo muestro en la práctica</td><td class="speaker-name">Italo Cruz - PE</td></tr>
                <tr><td>11:25 - 11:40<br />(15 min)</td><td>¿La IA sustituirá al humano en el diagnóstico radiológico de la endometriosis?</td><td class="speaker-name">Nadja Rolim - PE</td></tr>
                <tr><td>11:40 - 11:50<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td>11:50 - 13:30<br />(1 hora y 40 min)</td><td colspan="2" class="session-break"><strong>DESCANSO LIBRE</strong></td></tr>
                <tr><td>13:30 - 15:30<br />(2 horas)</td><td colspan="2" class="session-live"><strong>CIRUGÍAS EN VIVO - EN SALA A</strong></td></tr>
                <tr><td>15:30 - 16:00<br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td>16:00 - 16:15<br />(15 min)</td><td>SIMPOSIO BAYER - Tratamiento Clínico de la Endometriosis según el protocolo de la ACOH 2026</td><td class="speaker-name">Jardel Soares - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>16:15 - 17:55<br />(1 hora y<br />40 min)</strong><br />MESA 2 - En mi consultorio<br />Presidente: Simone Carvalho - PE <br />Debatientes: Leonardo Lima - PE, Érica</td></tr>
                <tr><td>16:15 - 16:35 <br />(20 min)</td><td>Climaterio y Menopausia en la paciente con Endometriosis. ¿Cómo conduzco caso por caso?</td><td class="speaker-name">Priscilla Vieira - PE</td></tr>
                <tr><td>16:35 - 16:55<br />(20 min)</td><td>Métodos de diagnóstico para endometriosis — ¿qué tenemos ya? ¿Cuáles son las nuevas perspectivas?</td><td class="speaker-name">Cicilia Pontes - PE</td></tr>
                <tr><td>16:55 - 17:15 <br />(20 min)</td><td>Endometriosis en la adolescencia: ¿cómo la conduzco? ¿Cómo evitar el exceso de cirugías?</td><td class="speaker-name">Lilia Mendes - CE</td></tr>
                <tr><td>17:15 - 17:35<br />(20 min)</td><td>Dolor en la relación sexual, vaginismo, dificultades de relación como secuela de la endometriosis. ¿Cómo conducir?</td><td class="speaker-name">Aleide Tavares - PE</td></tr>
                <tr><td>17:35 - 17:45<br />(10  min)</td><td>Impactos negativos de la endometriosis en la sociedad. ¿Cómo podemos revertir esto?</td><td class="speaker-name">Iolanda Matias - PE</td></tr>
                <tr><td>17:45 - 17:55<br />(10  min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td>17:55 - 18:40<br />(45 min)</td><td>¡USTED DECIDE!<br />Tomando decisiones en el tratamiento quirúrgico en ginecología<br />Coordinación: Iolanda Matias - PE</td><td></td></tr>
                <tr><td></td><td>Caso Clínico 1 - Endometriosis severa con exclusión renal</td><td class="speaker-name">Andréa Perez - SP</td></tr>
                <tr><td></td><td>Caso Clínico 2 - PROLAPSO + INCONTINENCIA URINARIA</td><td class="speaker-name">Sara Arcanjo - CE</td></tr>
                <tr><td></td><td>Caso Clínico 3 - ADENOMIOSIS</td><td class="speaker-name">Raquel Magalhães - SP</td></tr>
                <tr><td>18:40</td><td colspan="2" class="session-break"><strong>Cierre</strong></td></tr>""",
    "sch.satAudA": f"""
                <tr><td>08:00 - 10:00            (2 horas)</td><td colspan="2" class="session-live"><strong>CIRUGÍAS EN VIVO                                                                                                                                                                           Presidente: Iolanda Matias - PE</strong><div style="{DETAIL}">Debatientes:  Mariana Roma - PE, Felipe Rocha - PE, Guilherme Zanluchi - SP, Felipe Rocha - PB</div><div style="{DETAIL}">* Hospital Santa Joana Recife  - PE<br />Raquel Magalhães SP<br />Conducción del caso: Sidraiton Melo - PE <br /><br />* Hospital Barão de Lucena  - PE<br />Sara Arcanjo - CE <br />Andreisa Bilhar - CE <br />Conducción del caso: Eveline Martins Sampaio - PE <br /><br />* Hospital  Bragança Paulista <br />Dr. Rodrigo Sader Heck SP<br /><br />* Hospital Itaim Bibi - SP <br />Dr Paulo Ayroza /<br />Helizabeth Salomão</div></td></tr>
                <tr><td>10:00 - 10:30 <br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:30<br />(1 hora y<br />10 min)</strong><br />MESA 1 - Infertilidad y Endometriosis <br />Presidente:<br />Debatientes:</td></tr>
                <tr><td>10:30 - 10:45<br />(15 min)</td><td>¿Qué hacer primero en la paciente con endometriosis: FIV antes y después operar, u operar y después la FIV?</td><td class="speaker-name">Patrick Bellelis - SP<br />*Online*</td></tr>
                <tr><td>10:45 - 11:00<br />(15 min)</td><td>En la investigación histeroscópica de la mujer infértil: ¿qué debo buscar? ¿Cómo tratar?</td><td class="speaker-name">Altina Castelo Branco - PE</td></tr>
                <tr><td>11:00 - 11:15<br />(15 min)</td><td>El desafío del manejo de las malformaciones uterinas: del diagnóstico a la elección de la vía ideal de abordaje. ¿Cuál es la mejor estrategia quirúrgica?</td><td class="speaker-name">Mariana Vieira - SP<br />*Online*</td></tr>
                <tr><td>11:15 - 11:30<br />(15 min)</td><td>De la implantación al parto — ¿cambia algo en el seguimiento de la mujer que cursa con endometriosis e infertilidad?</td><td class="speaker-name">Edilberto Rocha - PE</td></tr>
                <tr><td>11:30 - 11:40 <br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>11:40 - 12:35<br />(55 min)</strong><br />Conferencias<br /> Presidente: Walter Ivo Paiva PE</td></tr>
                <tr><td>11:40 - 12:00<br />(20 min)</td><td>Conferencia: Cirugía Robótica en la Ginecología y otras tecnologías asociadas —<br />¿Qué beneficios ya tenemos comprobados?</td><td class="speaker-name">Jordanna Diniz - DF<br />*Online*</td></tr>
                <tr><td>12:00 - 12:20<br />(20 min)</td><td>Conferencia: Protocolo ERAS - ¿Se aplica incluso en cirugías de alta complejidad?</td><td class="speaker-name">Carlos Godoy - SP</td></tr>
                <tr><td>12:20 - 12:35<br />(15 min)</td><td>Conferencia: Manejo clínico del dolor - ¿Qué hay de nuevo? ¿Cannabis?<br />¿Y en el manejo avanzado del dolor qué hay de nuevo?</td><td class="speaker-name">Luiz Severo - PE</td></tr>
                <tr><td>12:35 - 12:55<br />(20 min)</td><td>SIMPOSIO ABIOCON</td><td class="speaker-name">Fernando Prado - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>12:55 - 13:35<br />(40 min)</strong><br />Conferencias<br /> Presidente: Jardel Soares - PE</td></tr>
                <tr><td>12:55 - 13:15<br />(20 min)</td><td>Lecciones para la vida: La supervivencia del cirujano videolaparoscópico y robótico — de la ergonomía a la salud mental</td><td class="speaker-name">Fernando Heredia - Chile <br />*Online*</td></tr>
                <tr><td>13:15 - 13:35<br />(20 min)</td><td>Lecciones para la vida: Decidir es más difícil que operar</td><td class="speaker-name">Ana Sierra - México <br />*Online*</td></tr>
                <tr><td colspan="3" class="session-header"><strong>13:35 - 14:25            (50 min)</strong><br />MESA 2 - Coloproctología en el panel<br />Presidente: Marcos Saturnino - PE<br />Debatientes: Gilberto Pagnissin - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>13:35 - 14:05            (30 min)</strong><br />TRIPLE CROSS FIRE o el TRIELO</td></tr>
                <tr><td></td><td>Shaving</td><td class="speaker-name">Paulo Mozart - PE</td></tr>
                <tr><td></td><td>Discoide y doble discoide</td><td class="speaker-name">Claudia Joaquim - RJ</td></tr>
                <tr><td></td><td>Resección segmentaria</td><td class="speaker-name">Renato Barretto - SP</td></tr>
                <tr><td>14:05 - 14:15            (10 min)</td><td>Dehiscencias intestinales — ¿cómo conducir?</td><td class="speaker-name">Cláudia Joaquim - RJ</td></tr>
                <tr><td>14:15 - 14:25            (10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td>14:25 - 14:35<br />(10 min)</td><td colspan="2" class="session-break"><strong>DESCANSO</strong></td></tr>
                <tr><td>14:35 - 16:15<br />(1 hora y 40 min)</td><td colspan="2" class="session-live"><strong>CIRUGÍAS EN VIVO                                                                                                                                                                                        Coordinador: Jardel Soares - PE</strong><div style="{DETAIL}">Debatientes: Sidraiton Melo - PE, Andreisa Bilhar - CE, Yole Minervino - PB</div><div style="{DETAIL}">* Hospital Santa Joana Recife - PE<br />Giuliano Borrelli - SP<br />Conducción del caso: <br /><br />* Hospital Barão de Lucena - PE<br />Fabio Ohara - SP <br />Conducción del caso:<br /><br />*Cúcuta - Colombia  <br />Santiago Machicado <br /><br />* CUSCO - Peru<br />Eric Arancibia<br /><br />*Hospital Mocelia - México <br />Armando Menocau</div></td></tr>
                <tr><td>16:15</td><td colspan="2" class="session-break"><strong>Cierre</strong></td></tr>
                <tr><td>16:30</td><td colspan="2" class="session-break"><strong>Feijoada (adhesión)</strong></td></tr>""",
    "sch.satAudB": f"""
                <tr><td>08:00 - 10:00</td><td colspan="2" class="session-live"><strong>CIRUGÍAS EN VIVO - SALA A</strong></td></tr>
                <tr><td>10:00 - 10:30 <br />(30 min)</td><td colspan="2" class="session-break"><strong>COFFEE BREAK</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>10:30  - 11:10<br />(40 min)</strong><br />Conferencias - Urología en acción<br />Presidente: Guilherme Lima - PE<br />Debatientes: Evandilson Guenes - PE, Rafael Oliveira - PE</td></tr>
                <tr><td>10:30 - 10:45<br />(15 min)</td><td>Tratamiento de la endometriosis ureteral — en pelvis congeladas, ¿existe una mejor técnica?<br />¿Existe superioridad en la vía de abordaje?</td><td class="speaker-name">Antônio César Cruz - PE</td></tr>
                <tr><td>10:45 - 11:00<br />(15 min)</td><td>Lesión vesical — límites de la resección. ¿Existen repercusiones a largo plazo?</td><td class="speaker-name">Arthur Farias - PB</td></tr>
                <tr><td>11:00 -11:10              <br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>11:10 - 11:40<br />(30 min)</strong><br />Conferencias<br />Presidente: Diogenes Fontão - PE</td></tr>
                <tr><td>11:10 - 11:25 <br />(15 min)</td><td>Conferencia: Cuándo el dolor pélvico es mucho más que la endometriosis</td><td class="speaker-name">Giuliano Borrelli - SP</td></tr>
                <tr><td>11:25 - 11:40            (15 min)</td><td>Conferencia: PBM (Patient Blood Management) — ¿Cómo preparar al paciente para la cirugía? ¿Hasta cuándo tolerar la anemia? ¿Cómo optimizar sus resultados quirúrgicos?</td><td class="speaker-name">Dahra Teles - PE</td></tr>
                <tr><td colspan="3" class="session-header"><strong>11:40 - 12:30<br />(50 min)</strong><br />MESA 1 - La multidisciplinariedad<br />Presidente: Juliana  Zaidan - PE<br />Debatientes: Natália  Fernandes - PE, Rita Santos - PE, Leonardo Lima - PE, Sirley Portela - PE</td></tr>
                <tr><td>11:40 - 11:50<br />(10 min)</td><td>¿La mejor dieta para la paciente con endometriosis? ¿Hay espacio para suplementos?</td><td class="speaker-name">Nara Parente - CE</td></tr>
                <tr><td>11:50 - 12:00<br />(10 min)</td><td>Fisioterapia pélvica antes y después de la cirugía. ¿Qué resultados tenemos comprobados?</td><td class="speaker-name">Isabella Frota - CE</td></tr>
                <tr><td>12:00 - 12:10<br />(10 min)</td><td>La acupuntura como tratamiento adyuvante en las patologías ginecológicas.</td><td class="speaker-name">Isaura Vieira  - PE</td></tr>
                <tr><td>12:10 - 12:20<br />(10 min)</td><td>Los impactos de la actividad física en el tratamiento de la endometriosis.<br />¿Cuál es el mejor ejercicio?</td><td class="speaker-name">Paulo Carvalho - PE</td></tr>
                <tr><td>12:20 - 12:30<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td>12:35 - 12:55<br />(20 min)</td><td>SIMPOSIO ABIOCON - (SALA A)</td><td></td></tr>
                <tr><td>12:55 - 13:40<br />(45 min)</td><td colspan="2" class="session-break"><strong>DESCANSO LIBRE</strong></td></tr>
                <tr><td colspan="3" class="session-header"><strong>13:40 - 14:20<br />(40 min)</strong><br />Uroginecología en Foco<br />Presidente: Eveline Martins Sampaio - PE<br />Debatientes: Sônia Lavínia - PE, Vanessa Freitas - PE, Arthur Rangel - PE, Guilherme Zanluchi - SP</td></tr>
                <tr><td>13:40 - 13:50<br />(10 min)</td><td>Estudio urodinámico — ¿cuándo solicitar? ¿cómo interpretar?</td><td class="speaker-name">Mônica Diniz - PE</td></tr>
                <tr><td>13:50 - 14:00<br />(10 min)</td><td>Tratamiento de las distopias genitales — ¿cuál es la mejor técnica? ¿Y los resultados? Te lo muestro en la práctica</td><td class="speaker-name">Sara Arcanjo - CE</td></tr>
                <tr><td>14:00 - 14:10<br />(10 min)</td><td>Incontinencia urinaria — ¿cómo conducir? ¿cuál es el momento de operar? Te lo mostraré en la práctica</td><td class="speaker-name">Andreisa Bilhar  - CE</td></tr>
                <tr><td>14:10 - 14:20<br />(10 min)</td><td colspan="2" class="session-break"><strong>Discusión</strong></td></tr>
                <tr><td>14:20 - 14:35<br />(15 min)</td><td colspan="2" class="session-break"><strong>DESCANSO</strong></td></tr>
                <tr><td>14:35 - 16:15<br />(1 hora y 40 min)</td><td colspan="2" class="session-live"><strong>CIRUGÍAS EN VIVO - SALA A</strong></td></tr>
                <tr><td>16:15</td><td colspan="2" class="session-break"><strong>Cierre</strong></td></tr>
                <tr><td>16:30</td><td colspan="2" class="session-break"><strong>Feijoada (adhesión)</strong></td></tr>""",
}


def replace_lang_block(html: str, lang: str, updates: dict[str, str]) -> str:
    # Find the language object: en: { ... }, or es: { ... },
    lang_pat = rf"({lang}:\s*\{{)"
    m = re.search(lang_pat, html)
    if not m:
        raise SystemExit(f"language block {lang} not found")
    start = m.start()
    # Find matching closing brace of this language object by nesting count from m.end()-1
    i = m.end() - 1
    depth = 0
    end = None
    while i < len(html):
        ch = html[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
        i += 1
    if end is None:
        raise SystemExit(f"could not find end of {lang} block")
    block = html[start:end]
    for key, value in updates.items():
        pattern = rf'("{re.escape(key)}":\s*`)(.*?)(`)'
        block, n = re.subn(pattern, lambda m, v=value: f"{m.group(1)}{v}{m.group(3)}", block, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f"{lang}.{key} replace failed ({n})")
    return html[:start] + block + html[end:]


def main():
    html = INDEX.read_text(encoding="utf-8")
    html = replace_lang_block(html, "en", EN)
    html = replace_lang_block(html, "es", ES)
    INDEX.write_text(html, encoding="utf-8")
    print("Patched EN/ES schedule i18n keys:", ", ".join(EN))


if __name__ == "__main__":
    main()
