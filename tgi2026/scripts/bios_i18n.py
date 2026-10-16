"""English and Spanish résumé lines.

Keys are the Portuguese lines after generate_content.fix_bio(), so a change
in resumes.csv fails the build instead of leaving Portuguese on the English
and Spanish pages. Names of people, hospitals and acronyms stay as written.
"""

BIOS = {
    "Coordenador do Jayme da Fonte diagnósticos": {
        "en": "Coordinator of Jayme da Fonte Diagnósticos",
        "es": "Coordinador de Jayme da Fonte Diagnósticos",
    },
    "Membro da comissão científica do colégio brasileiro de radiologia": {
        "en": "Member of the scientific committee of the Brazilian College of Radiology",
        "es": "Miembro de la comisión científica del Colegio Brasileño de Radiología",
    },
    "Professor adjunto de cirurgia da Universidade de Pernambuco. Preceptor da Residência em Cirurgia Geral e Digestiva da Universidade de Pernambuco. Cirurgião transplantador de fígado do Hospital Universitário Osvaldo Cruz e do Hospital Nossa Senhora das Neves": {
        "en": "Adjunct professor of surgery at the University of Pernambuco. Preceptor of the General and Digestive Surgery Residency at the University of Pernambuco. Liver transplant surgeon at Hospital Universitário Osvaldo Cruz and Hospital Nossa Senhora das Neves",
        "es": "Profesor adjunto de cirugía de la Universidad de Pernambuco. Preceptor de la Residencia de Cirugía General y Digestiva de la Universidad de Pernambuco. Cirujano de trasplante hepático del Hospital Universitário Osvaldo Cruz y del Hospital Nossa Senhora das Neves",
    },
    "Radiologista Rede D'Or": {
        "en": "Radiologist at Rede D'Or",
        "es": "Radióloga en Rede D'Or",
    },
    "Coordenadora Radiologia HSE": {
        "en": "Radiology coordinator at HSE",
        "es": "Coordinadora de Radiología del HSE",
    },
    "Membro Titular CBR": {
        "en": "Full member of the CBR",
        "es": "Miembro titular del CBR",
    },
    "Oncologista Clínico Do Hospital Santa Joana – Rede Américas": {
        "en": "Clinical oncologist at Hospital Santa Joana – Rede Américas",
        "es": "Oncólogo clínico del Hospital Santa Joana – Rede Américas",
    },
    "Professor da UPE": {
        "en": "Professor at UPE",
        "es": "Profesor de la UPE",
    },
    "Cirurgiã geral Pela universidade Federal do Rio Grande do Norte - HUOL": {
        "en": "General surgeon, trained at the Federal University of Rio Grande do Norte – HUOL",
        "es": "Cirujana general, formada en la Universidad Federal de Rio Grande do Norte – HUOL",
    },
    "Cirurgiã oncológica pelo hospital do câncer de Pernambuco": {
        "en": "Surgical oncologist at Hospital do Câncer de Pernambuco",
        "es": "Cirujana oncológica del Hospital do Câncer de Pernambuco",
    },
    "Preceptora do serviço de oncoginecologia do Hospital do Câncer de Pernambuco": {
        "en": "Preceptor in the gynaecological oncology service at Hospital do Câncer de Pernambuco",
        "es": "Preceptora del servicio de oncología ginecológica del Hospital do Câncer de Pernambuco",
    },
    "Cirurgiã oncológica do grupo Américas - Hospital Santa Joana": {
        "en": "Surgical oncologist with Grupo Américas – Hospital Santa Joana",
        "es": "Cirujana oncológica del Grupo Américas – Hospital Santa Joana",
    },
    "Fundador e diretor geral da Angiorad": {
        "en": "Founder and general director of Angiorad",
        "es": "Fundador y director general de Angiorad",
    },
    "Fundador e ex-presidente da Sociedade Brasileira de Radiologia": {
        "en": "Founder and former president of the Brazilian Society of Radiology",
        "es": "Fundador y expresidente de la Sociedad Brasileña de Radiología",
    },
    "Intervencionista e Cirurgião Endovascular": {
        "en": "Interventional and endovascular surgeon",
        "es": "Intervencionista y cirujano endovascular",
    },
    "Chefe da Radiologia Intervencionista do Real Hospital Português": {
        "en": "Head of Interventional Radiology at Real Hospital Português",
        "es": "Jefe de Radiología Intervencionista del Real Hospital Português",
    },
    "Médica graduada pela Universidade Federal de Pernambuco - UFPE": {
        "en": "Physician, graduated from the Federal University of Pernambuco – UFPE",
        "es": "Médica, graduada en la Universidad Federal de Pernambuco – UFPE",
    },
    "Residência em Clínica médica e Hepatologia": {
        "en": "Residency in internal medicine and hepatology",
        "es": "Residencia en clínica médica y hepatología",
    },
    "Hepatologista do Hospital Santa Joana Recife e Hospital Esperança Recife": {
        "en": "Hepatologist at Hospital Santa Joana Recife and Hospital Esperança Recife",
        "es": "Hepatóloga del Hospital Santa Joana Recife y del Hospital Esperança Recife",
    },
    "Preceptora da residência de Clínica médica do Hospital Esperança Recife - rede D’Or": {
        "en": "Preceptor of the internal medicine residency at Hospital Esperança Recife – Rede D'Or",
        "es": "Preceptora de la residencia de clínica médica del Hospital Esperança Recife – Rede D'Or",
    },
    "Ex residente de oncologia clínica do INCA": {
        "en": "Former clinical oncology resident at INCA",
        "es": "Exresidenta de oncología clínica del INCA",
    },
    "Oncologista clínico da Onkos": {
        "en": "Clinical oncologist at Onkos",
        "es": "Oncóloga clínica de Onkos",
    },
    "Presidente e voluntária do Instituto Cristina Tavares": {
        "en": "President and volunteer of Instituto Cristina Tavares",
        "es": "Presidenta y voluntaria del Instituto Cristina Tavares",
    },
    "Mãe de Pedro, Luísa e Júlia": {
        "en": "Mother of Pedro, Luísa and Júlia",
        "es": "Madre de Pedro, Luísa y Júlia",
    },
    "Avó de Fernanda": {
        "en": "Grandmother of Fernanda",
        "es": "Abuela de Fernanda",
    },
    "Oncologista do Hospital Santa Joana e do Hospital Universitário Oswaldo Cruz / UPE": {
        "en": "Oncologist at Hospital Santa Joana and Hospital Universitário Oswaldo Cruz / UPE",
        "es": "Oncóloga del Hospital Santa Joana y del Hospital Universitário Oswaldo Cruz / UPE",
    },
    "Preceptora de graduação e pós-graduação da FCM - Faculdade de Ciências Médicas / UPE": {
        "en": "Preceptor for undergraduate and postgraduate students at FCM – Faculdade de Ciências Médicas / UPE",
        "es": "Preceptora de grado y posgrado de la FCM – Faculdade de Ciências Médicas / UPE",
    },
    "Mestre pela UPE": {
        "en": "Master's degree from UPE",
        "es": "Magíster por la UPE",
    },
    "Doutoranda em medicina translacional pela UNIFESP.": {
        "en": "PhD candidate in translational medicine at UNIFESP.",
        "es": "Doctoranda en medicina traslacional por la UNIFESP.",
    },
    "Enfermeira graduada pela Universidade de Pernambuco.": {
        "en": "Nurse, graduated from the University of Pernambuco.",
        "es": "Enfermera, graduada en la Universidad de Pernambuco.",
    },
    "Atua como Enfermeira navegadora da linha de cuidados em Tumores GastroIntestinais (TGI) do Hospital Santa Joana Recife.": {
        "en": "Nurse navigator for the gastrointestinal tumour (GI) care pathway at Hospital Santa Joana Recife.",
        "es": "Enfermera navegadora de la línea de cuidado de tumores gastrointestinales (TGI) del Hospital Santa Joana Recife.",
    },
    "Oncologista clínico Rede Americas, IMIP, HBL": {
        "en": "Clinical oncologist at Rede Américas, IMIP and HBL",
        "es": "Oncólogo clínico de Rede Américas, IMIP y HBL",
    },
    "PhD pela Unifesp": {
        "en": "PhD from Unifesp",
        "es": "Doctorado por la Unifesp",
    },
    "Médica Nutróloga - Título de especialista ABRAN/CFM": {
        "en": "Nutrition physician – specialist title from ABRAN/CFM",
        "es": "Médica nutrióloga – título de especialista ABRAN/CFM",
    },
    "Especialista em terapia parenteral e enteral - SBNPE/CFM": {
        "en": "Specialist in parenteral and enteral therapy – SBNPE/CFM",
        "es": "Especialista en terapia parenteral y enteral – SBNPE/CFM",
    },
    "Residência em Clínica médica - Santa casa de misericórdia do Recife": {
        "en": "Residency in internal medicine – Santa Casa de Misericórdia do Recife",
        "es": "Residencia en clínica médica – Santa Casa de Misericórdia do Recife",
    },
    "Coordenadora da equipe de terapia nutricional e do serviço de nutrologia do hospital Santa Joana": {
        "en": "Coordinator of the nutrition therapy team and the clinical nutrition service at Hospital Santa Joana",
        "es": "Coordinadora del equipo de terapia nutricional y del servicio de nutriología del Hospital Santa Joana",
    },
    "Oncologista do Grupo Américas": {
        "en": "Oncologist at Grupo Américas",
        "es": "Oncólogo del Grupo Américas",
    },
    "Oncologista e preceptor da residência da oncologia do Hospital do Câncer de Pe.": {
        "en": "Oncologist and preceptor of the oncology residency at Hospital do Câncer de Pernambuco.",
        "es": "Oncólogo y preceptor de la residencia de oncología del Hospital do Câncer de Pernambuco.",
    },
    "Oncologista do Hospital Barão de Lucena": {
        "en": "Oncologist at Hospital Barão de Lucena",
        "es": "Oncólogo del Hospital Barão de Lucena",
    },
    "Professor Adjunto de Cirurgia Abdominal da Universidade Federal de Pernambuco": {
        "en": "Adjunct professor of abdominal surgery at the Federal University of Pernambuco",
        "es": "Profesor adjunto de cirugía abdominal de la Universidad Federal de Pernambuco",
    },
    "Cirurgião do Real Instituto de Cirurgia Oncológica - Hospital Português - Recife": {
        "en": "Surgeon at the Real Instituto de Cirurgia Oncológica – Hospital Português – Recife",
        "es": "Cirujano del Real Instituto de Cirurgia Oncológica – Hospital Português – Recife",
    },
    "Supervisor da Residência de Cirurgia Geral do Hospital da Restauração - Recife": {
        "en": "Supervisor of the General Surgery Residency at Hospital da Restauração – Recife",
        "es": "Supervisor de la Residencia de Cirugía General del Hospital da Restauração – Recife",
    },
    "Titular do CBCD, do CBC e da ABCG": {
        "en": "Full member of the CBCD, the CBC and the ABCG",
        "es": "Miembro titular del CBCD, del CBC y de la ABCG",
    },
    "Proctor em Cirurgia Robótica pelo CBC": {
        "en": "Robotic surgery proctor for the CBC",
        "es": "Proctor en cirugía robótica por el CBC",
    },
    "Graduação em medicina pela Universidade Federal de Pernambuco (UFPE)": {
        "en": "Medical degree from the Federal University of Pernambuco (UFPE)",
        "es": "Graduación en medicina por la Universidad Federal de Pernambuco (UFPE)",
    },
    "Residência médica em Radioterapia no IMIP": {
        "en": "Medical residency in radiation oncology at IMIP",
        "es": "Residencia médica en radioterapia en el IMIP",
    },
    "Membro titular da Sociedade Brasileira de radioterapia": {
        "en": "Full member of the Brazilian Society of Radiation Oncology",
        "es": "Miembro titular de la Sociedad Brasileña de Radioterapia",
    },
    "Rádio-oncologista do HUOC-PE (Hospital Universitário Oswaldo Cruz) e da Oncoclínicas Radioterapia Recife , sendo também responsável Técnico deste último.": {
        "en": "Radiation oncologist at HUOC-PE (Hospital Universitário Oswaldo Cruz) and at Oncoclínicas Radioterapia Recife, where he is also the technical lead.",
        "es": "Radioncólogo del HUOC-PE (Hospital Universitário Oswaldo Cruz) y de Oncoclínicas Radioterapia Recife, donde también es el responsable técnico.",
    },
    "Cirurgião do Aparelho Digestivo do Santa Joana, Ebserh e Hospital dos Servidores.": {
        "en": "Digestive tract surgeon at Santa Joana, Ebserh and Hospital dos Servidores.",
        "es": "Cirujano del aparato digestivo del Santa Joana, Ebserh y Hospital dos Servidores.",
    },
    "Especialização em Clínica médica no Hospital das Clínicas - UFPE": {
        "en": "Specialist training in internal medicine at Hospital das Clínicas – UFPE",
        "es": "Especialización en clínica médica en el Hospital das Clínicas – UFPE",
    },
    "Especialização em Oncologia Clínica no Real Hospital Português da beneficência em Pernambuco": {
        "en": "Specialist training in clinical oncology at Real Hospital Português de Beneficência em Pernambuco",
        "es": "Especialización en oncología clínica en el Real Hospital Português de Beneficência em Pernambuco",
    },
    "Oncologista clínico pela Unionco Recife e Rede Americas": {
        "en": "Clinical oncologist at Unionco Recife and Rede Américas",
        "es": "Oncólogo clínico de Unionco Recife y Rede Américas",
    },
    "VP de oncologia da Rede Américas.": {
        "en": "Vice president of oncology at Rede Américas.",
        "es": "Vicepresidente de oncología de Rede Américas.",
    },
    "Fellowship em Oncologia Gastrointestinal pelo Memorial Sloan Kettering Cancer Center": {
        "en": "Fellowship in gastrointestinal oncology at Memorial Sloan Kettering Cancer Center",
        "es": "Fellowship en oncología gastrointestinal en el Memorial Sloan Kettering Cancer Center",
    },
    "Ex-presidente da SBOC(sociedade brasileira de oncologia clínica)": {
        "en": "Former president of the SBOC (Brazilian Society of Clinical Oncology)",
        "es": "Expresidente de la SBOC (Sociedad Brasileña de Oncología Clínica)",
    },
    "Graduação pela UFPE, mestrando e professor substituto na mesma instituição.": {
        "en": "Graduate of UFPE, master's student and substitute professor at the same institution.",
        "es": "Graduado por la UFPE, estudiante de maestría y profesor sustituto en la misma institución.",
    },
    "Residência médica na EPM(escola paulista de medicina)/UNIFESP.": {
        "en": "Medical residency at EPM (Escola Paulista de Medicina)/UNIFESP.",
        "es": "Residencia médica en la EPM (Escola Paulista de Medicina)/UNIFESP.",
    },
    "Trabalha no Hospital Otávio de Freitas e também nos laboratórios SPAC e Citomaxx.": {
        "en": "Works at Hospital Otávio de Freitas and also at the SPAC and Citomaxx laboratories.",
        "es": "Trabaja en el Hospital Otávio de Freitas y también en los laboratorios SPAC y Citomaxx.",
    },
    "Médico do ambulatório de Pâncreas e doença inflamatória intestinal ( HC-UFPE )": {
        "en": "Physician in the pancreas and inflammatory bowel disease clinic (HC-UFPE)",
        "es": "Médico del ambulatorio de páncreas y enfermedad inflamatoria intestinal (HC-UFPE)",
    },
    "Membro titular da FBG ( Federação Brasileira de Gastroenterologia)": {
        "en": "Full member of the FBG (Brazilian Federation of Gastroenterology)",
        "es": "Miembro titular de la FBG (Federación Brasileña de Gastroenterología)",
    },
    "Membro titular do Gediib ( Grupo de estudo da doença inflamatória intestinal)": {
        "en": "Full member of Gediib (Inflammatory Bowel Disease Study Group)",
        "es": "Miembro titular del Gediib (Grupo de estudio de la enfermedad inflamatoria intestinal)",
    },
    "Professor da disciplina de Gastroenterologia ( Uninassau )": {
        "en": "Professor of gastroenterology (Uninassau)",
        "es": "Profesor de la disciplina de Gastroenterología (Uninassau)",
    },
    "Oncologista clínico do Hospital Santa Joana e Onkos.": {
        "en": "Clinical oncologist at Hospital Santa Joana and Onkos.",
        "es": "Oncólogo clínico del Hospital Santa Joana y de Onkos.",
    },
    "Preceptor da Residência médica em Oncologia do Hospital de câncer de Pernambuco.": {
        "en": "Preceptor of the medical oncology residency at Hospital de Câncer de Pernambuco.",
        "es": "Preceptor de la residencia médica en oncología del Hospital de Câncer de Pernambuco.",
    },
    "Coordenador da Residência médica em Oncologia Clínica do Santa Joana": {
        "en": "Coordinator of the clinical oncology residency at Santa Joana",
        "es": "Coordinador de la residencia médica en oncología clínica del Santa Joana",
    },
    "Oncologista Clínica Hospital Santa Joana Rede Américas": {
        "en": "Clinical oncologist at Hospital Santa Joana, Rede Américas",
        "es": "Oncóloga clínica del Hospital Santa Joana, Rede Américas",
    },
    "Médico cirurgião, especialista em Cirurgia Geral, Cirurgia do Aparelho Digestivo, minimamente invasivas e robóticas.": {
        "en": "Surgeon, specialist in general surgery, digestive tract surgery, and minimally invasive and robotic surgery.",
        "es": "Médico cirujano, especialista en cirugía general, cirugía del aparato digestivo y cirugía mínimamente invasiva y robótica.",
    },
    "Chefe da Emergência e Preceptor das Residências Médicas de Cirurgia Geral e Cirurgia do Aparelho Digestivo do Hospital Getúlio Vargas (HGV). Atua também como cirurgião das clínicas Cirúrgica e Digest.": {
        "en": "Head of the Emergency Department and preceptor of the General Surgery and Digestive Tract Surgery residencies at Hospital Getúlio Vargas (HGV). Also a surgeon at Clínica Cirúrgica and Clínica Digest.",
        "es": "Jefe de Urgencias y preceptor de las residencias médicas de Cirugía General y Cirugía del Aparato Digestivo del Hospital Getúlio Vargas (HGV). También actúa como cirujano de las clínicas Cirúrgica y Digest.",
    },
    "Enfermeira pela Universidade Federal de Pernambuco": {
        "en": "Nurse, Federal University of Pernambuco",
        "es": "Enfermera por la Universidad Federal de Pernambuco",
    },
    "Residência em Oncologia pela Universidade de Pernambuco": {
        "en": "Oncology residency at the University of Pernambuco",
        "es": "Residencia en oncología por la Universidad de Pernambuco",
    },
    "Enfermeira Navegadora em Oncologia do Hospital Santa Joana Recife": {
        "en": "Oncology nurse navigator at Hospital Santa Joana Recife",
        "es": "Enfermera navegadora en oncología del Hospital Santa Joana Recife",
    },
    "Radiologista Abdominal e Oncorradiologista pela Beneficência Portuguesa de São Paulo.": {
        "en": "Abdominal radiologist and oncologic radiologist, trained at Beneficência Portuguesa de São Paulo.",
        "es": "Radiólogo abdominal y oncorradiólogo por la Beneficência Portuguesa de São Paulo.",
    },
    "Radiologista do Hospital Santa Joana": {
        "en": "Radiologist at Hospital Santa Joana",
        "es": "Radiólogo del Hospital Santa Joana",
    },
    "Preceptor da residência médica em radiologia e diagnóstico por imagem do Hospital da Restauração.": {
        "en": "Preceptor of the medical residency in radiology and diagnostic imaging at Hospital da Restauração.",
        "es": "Preceptor de la residencia médica en radiología y diagnóstico por imagen del Hospital da Restauração.",
    },
    "Criador do perfil educacional e pós graduação @radiologiabdominal": {
        "en": "Creator of the educational and postgraduate profile @radiologiabdominal",
        "es": "Creador del perfil educativo y de posgrado @radiologiabdominal",
    },
    "Residência em Oncologia Clínica pelo IMIP": {
        "en": "Residency in clinical oncology at IMIP",
        "es": "Residencia en oncología clínica por el IMIP",
    },
    "Oncologista Clínico da Rede Américas e do Hospital do Câncer de Pernambuco": {
        "en": "Clinical oncologist at Rede Américas and Hospital do Câncer de Pernambuco",
        "es": "Oncólogo clínico de Rede Américas y del Hospital do Câncer de Pernambuco",
    },
    "Pós-Graduação em cuidados Paliativos pela Santa Casa de Misericórdia da Bahia": {
        "en": "Postgraduate degree in palliative care from Santa Casa de Misericórdia da Bahia",
        "es": "Posgrado en cuidados paliativos por la Santa Casa de Misericórdia da Bahia",
    },
    "Membro Titular da Sociedade Brasileira de Radiologia Intervencionista e Cirurgia Endovascular - SOBRICE": {
        "en": "Full member of the Brazilian Society of Interventional Radiology and Endovascular Surgery – SOBRICE",
        "es": "Miembro titular de la Sociedad Brasileña de Radiología Intervencionista y Cirugía Endovascular – SOBRICE",
    },
    "Radiologista Intervencionista e Cirurgião Vascular do IMIP, Barão de Lucena e Angiorad": {
        "en": "Interventional radiologist and vascular surgeon at IMIP, Barão de Lucena and Angiorad",
        "es": "Radiólogo intervencionista y cirujano vascular del IMIP, Barão de Lucena y Angiorad",
    },
    "Oncologista clínico do Hospital Santa Joana Recife (Americas Oncologia) e do Hospital Universitário Oswaldo Cruz (Universidade de Pernambuco)": {
        "en": "Clinical oncologist at Hospital Santa Joana Recife (Américas Oncologia) and Hospital Universitário Oswaldo Cruz (University of Pernambuco)",
        "es": "Oncólogo clínico del Hospital Santa Joana Recife (Américas Oncologia) y del Hospital Universitário Oswaldo Cruz (Universidad de Pernambuco)",
    },
    "Ex-research FELLOWSHIP IOSI, Switzerland": {
        "en": "Former research fellow, IOSI, Switzerland",
        "es": "Ex research fellowship en el IOSI, Suiza",
    },
    "Prof titular de gastroenterologia - FCM/UPE": {
        "en": "Full professor of gastroenterology – FCM/UPE",
        "es": "Profesora titular de gastroenterología – FCM/UPE",
    },
    "Chefe do serviço de gastrohepatologia - HUOC/UPE": {
        "en": "Head of the gastro-hepatology service – HUOC/UPE",
        "es": "Jefa del servicio de gastrohepatología – HUOC/UPE",
    },
    "Presidente do Instituto e transplantes de PE": {
        "en": "President of the Pernambuco Transplant Institute",
        "es": "Presidenta del Instituto de Trasplantes de Pernambuco",
    },
    "Gastrohepatologista do Hospital Santa Joana": {
        "en": "Gastro-hepatologist at Hospital Santa Joana",
        "es": "Gastrohepatóloga del Hospital Santa Joana",
    },
    "Coordenadora da hepatologia do Imip": {
        "en": "Hepatology coordinator at IMIP",
        "es": "Coordinadora de hepatología del IMIP",
    },
    "Mestre em Medicina tropical pela UFPE": {
        "en": "Master's degree in tropical medicine from UFPE",
        "es": "Magíster en medicina tropical por la UFPE",
    },
    "Preceptor da Residência de Oncologia Clínica do IMIP": {
        "en": "Preceptor of the Clinical Oncology Residency at IMIP",
        "es": "Preceptor de la Residencia de Oncología Clínica del IMIP",
    },
    "Médico Oncologista da Rede Americas.": {
        "en": "Medical oncologist at Rede Américas.",
        "es": "Médico oncólogo de Rede Américas.",
    },
    "Médico Oncologista no IONE": {
        "en": "Medical oncologist at IONE",
        "es": "Médico oncólogo en el IONE",
    },
    "Cirurgião Oncológico": {
        "en": "Surgical oncologist",
        "es": "Cirujano oncólogo",
    },
    "Titular da SBCO": {
        "en": "Full member of the SBCO",
        "es": "Miembro titular de la SBCO",
    },
    "Preceptor da residência de cirurgia Oncológica IMIP": {
        "en": "Preceptor of the surgical oncology residency at IMIP",
        "es": "Preceptor de la residencia de cirugía oncológica del IMIP",
    },
    "Preceptor de residência Cirurgia Geral Hospital Barão de Lucena": {
        "en": "Preceptor of the general surgery residency at Hospital Barão de Lucena",
        "es": "Preceptor de la residencia de cirugía general del Hospital Barão de Lucena",
    },
    "Cirurgião Oncológico Rede D’Or São Luiz - Memorial São José e Memorial Star": {
        "en": "Surgical oncologist at Rede D'Or São Luiz – Memorial São José and Memorial Star",
        "es": "Cirujano oncólogo de Rede D'Or São Luiz – Memorial São José y Memorial Star",
    },
    "CirurgiãoVideolaparoscópico e Cirugião Robótico": {
        "en": "Laparoscopic and robotic surgeon",
        "es": "Cirujano videolaparoscópico y robótico",
    },
    "Cirurgião Oncológico Santa Joana": {
        "en": "Surgical oncologist at Santa Joana",
        "es": "Cirujano oncólogo del Santa Joana",
    },
    "Nutricionista pela UFPE": {
        "en": "Dietitian, UFPE",
        "es": "Nutricionista por la UFPE",
    },
    "Pós graduada em nutrição clínica pelo IMIP": {
        "en": "Postgraduate degree in clinical nutrition from IMIP",
        "es": "Posgrado en nutrición clínica por el IMIP",
    },
    "Especialista em Nutrição Oncológica pela SBNO": {
        "en": "Specialist in oncology nutrition, SBNO",
        "es": "Especialista en nutrición oncológica por la SBNO",
    },
    "Doutoranda e Mestre em Nutrição pela UFPE": {
        "en": "PhD candidate and holder of a master's degree in nutrition from UFPE",
        "es": "Doctoranda y magíster en nutrición por la UFPE",
    },
    "Nutricionista do ambulatório de oncologia do hospital das clínicas de Pernambuco": {
        "en": "Dietitian in the oncology clinic at Hospital das Clínicas de Pernambuco",
        "es": "Nutricionista del ambulatorio de oncología del Hospital das Clínicas de Pernambuco",
    },
    "Atendimento em consultório particular": {
        "en": "Private practice",
        "es": "Atención en consultorio particular",
    },
    "Professora de pós graduação": {
        "en": "Postgraduate lecturer",
        "es": "Profesora de posgrado",
    },
    "Membro Titular da Sociedade Brasileira de Coloproctologia": {
        "en": "Full member of the Brazilian Society of Coloproctology",
        "es": "Miembro titular de la Sociedad Brasileña de Coloproctología",
    },
    "Coloproctologista do Real Hospital Português": {
        "en": "Colorectal surgeon at Real Hospital Português",
        "es": "Coloproctólogo del Real Hospital Português",
    },
    "Médico Radiologista com título de especialista pelo CBR": {
        "en": "Radiologist with a specialist title from the CBR",
        "es": "Radióloga con título de especialista del CBR",
    },
    "Mestrado pela UFPE": {
        "en": "Master's degree from UFPE",
        "es": "Maestría por la UFPE",
    },
    "Pós graduação em medicina interna e saúde da mulher": {
        "en": "Postgraduate training in internal medicine and women's health",
        "es": "Posgrado en medicina interna y salud de la mujer",
    },
    "Preceptora de radiologia no HC e HGV": {
        "en": "Radiology preceptor at HC and HGV",
        "es": "Preceptora de radiología en el HC y el HGV",
    },
    "Oncologista pelo Hospital Sírio Libanês (SP).": {
        "en": "Oncologist, trained at Hospital Sírio-Libanês (SP).",
        "es": "Oncólogo por el Hospital Sírio-Libanês (SP).",
    },
    "Oncologista do Hospital Santa Joana": {
        "en": "Oncologist at Hospital Santa Joana",
        "es": "Oncólogo del Hospital Santa Joana",
    },
    "Graduação em Medicina na Universidade de Pernambuco (2013); Pós-graduação em Cirurgia Geral com aperfeiçoamento em videolaparoscopia no Hospital Getúlio Vargas - Recife-PE (2016-2019) e em Cirurgia do Aparelho Digestivo pelo Hospital Universitário de Sergipe-Ebserh (2020-2022). Cirurgião e preceptor do serviço de Cirurgia Geral do Hospital Agamenon Magalhães e do serviço de Cirurgia Geral e Aparelho Digestivo do Hospital Universitário Oswaldo Cruz - HUOC em Recife-PE. Mestrando no programa de pós-graduação em cirurgia da Universidade Federal de Pernambuco (UFPE)": {
        "en": "Medical degree from the University of Pernambuco (2013). Postgraduate training in general surgery, with further training in laparoscopy, at Hospital Getúlio Vargas – Recife/PE (2016–2019), and in digestive tract surgery at Hospital Universitário de Sergipe–Ebserh (2020–2022). Surgeon and preceptor in the general surgery service at Hospital Agamenon Magalhães and in the general and digestive tract surgery service at Hospital Universitário Oswaldo Cruz – HUOC, Recife/PE. Master's student in the graduate programme in surgery at the Federal University of Pernambuco (UFPE)",
        "es": "Graduación en medicina en la Universidad de Pernambuco (2013). Posgrado en cirugía general, con perfeccionamiento en videolaparoscopia, en el Hospital Getúlio Vargas – Recife/PE (2016–2019), y en cirugía del aparato digestivo por el Hospital Universitário de Sergipe–Ebserh (2020–2022). Cirujano y preceptor del servicio de Cirugía General del Hospital Agamenon Magalhães y del servicio de Cirugía General y Aparato Digestivo del Hospital Universitário Oswaldo Cruz – HUOC, en Recife/PE. Estudiante de maestría en el programa de posgrado en cirugía de la Universidad Federal de Pernambuco (UFPE)",
    },
    "Professor Adjunto de Cirurgia da UPE": {
        "en": "Adjunct professor of surgery at UPE",
        "es": "Profesor adjunto de cirugía de la UPE",
    },
    "Professor de medicina de emergência da UNINASSAU": {
        "en": "Professor of emergency medicine at UNINASSAU",
        "es": "Profesor de medicina de urgencias de la UNINASSAU",
    },
    "Cirurgião do Aparelho Digestivo e Transplante de Fígado HUOC, HCP e HSJ": {
        "en": "Digestive tract and liver transplant surgeon at HUOC, HCP and HSJ",
        "es": "Cirujano del aparato digestivo y de trasplante hepático en el HUOC, HCP y HSJ",
    },
    "Cirurgião Geral e do Aparelho Digestivo do Hospital Santa Joana Recife": {
        "en": "General and digestive tract surgeon at Hospital Santa Joana Recife",
        "es": "Cirujano general y del aparato digestivo del Hospital Santa Joana Recife",
    },
    "Coordenador Médico da Linha Cirúrgica do Hospital Santa Joana.": {
        "en": "Medical coordinator of the surgical pathway at Hospital Santa Joana.",
        "es": "Coordinador médico de la línea quirúrgica del Hospital Santa Joana.",
    },
    "Coordenador médico do Bloco Cirúrgico do Hospital Alfa": {
        "en": "Medical coordinator of the operating theatre at Hospital Alfa",
        "es": "Coordinador médico del bloque quirúrgico del Hospital Alfa",
    },
    "Professor Titular da Universidade Federal de Pernambuco.": {
        "en": "Full professor at the Federal University of Pernambuco.",
        "es": "Profesor titular de la Universidad Federal de Pernambuco.",
    },
    "Pós doutorado em Biologia aplicada a Saúde - LIKA.": {
        "en": "Postdoctoral training in biology applied to health – LIKA.",
        "es": "Posdoctorado en biología aplicada a la salud – LIKA.",
    },
    "Chefe do Serviço de Promoção de Saúde e Qualidade de Vida - HC/UFPE/HUBrasil.": {
        "en": "Head of the Health Promotion and Quality of Life Service – HC/UFPE/HUBrasil.",
        "es": "Jefe del Servicio de Promoción de la Salud y Calidad de Vida – HC/UFPE/HUBrasil.",
    },
    "Membro da COESAS - Sociedade Brasileira de Cirurgia Bariátrica e Metabólica.": {
        "en": "Member of COESAS – Brazilian Society of Bariatric and Metabolic Surgery.",
        "es": "Miembro de la COESAS – Sociedad Brasileña de Cirugía Bariátrica y Metabólica.",
    },
    "Docente Permanente do Programas de Pós Graduação em Educação Física e Cirurgia da UFPE.": {
        "en": "Permanent faculty member of the graduate programmes in Physical Education and Surgery at UFPE.",
        "es": "Docente permanente de los programas de posgrado en Educación Física y Cirugía de la UFPE.",
    },
    "Mais de 30 anos Elabora e Prescreve programas de Treinamento para pessoas portadoras de doenças crônicas não transmissíveis.": {
        "en": "For more than 30 years he has designed and prescribed training programmes for people with chronic non-communicable diseases.",
        "es": "Durante más de 30 años elabora y prescribe programas de entrenamiento para personas con enfermedades crónicas no transmisibles.",
    },
    "Especialista em programas de treinamento especializados para redução da inflamação e dor.": {
        "en": "Specialist in training programmes for reducing inflammation and pain.",
        "es": "Especialista en programas de entrenamiento orientados a reducir la inflamación y el dolor.",
    },
    "Médico formado pela UPE": {
        "en": "Physician, graduated from UPE",
        "es": "Médico, formado por la UPE",
    },
    "Residência de Cir Oncologica pelo INCA": {
        "en": "Surgical oncology residency at INCA",
        "es": "Residencia de cirugía oncológica por el INCA",
    },
    "Coordenador do departamento de cirurgia oncologica do HUOC/ UPE": {
        "en": "Coordinator of the surgical oncology department at HUOC/UPE",
        "es": "Coordinador del departamento de cirugía oncológica del HUOC/UPE",
    },
    "Preceptor no programa de residência do HCP": {
        "en": "Preceptor on the residency programme at HCP",
        "es": "Preceptor en el programa de residencia del HCP",
    },
    "Cirurgião pelo Grupo COP/ Oncologia D'Or": {
        "en": "Surgeon with Grupo COP / Oncologia D'Or",
        "es": "Cirujano del Grupo COP / Oncologia D'Or",
    },
    "Cirurgião do aparelho digestivo formado na UFPE 1984": {
        "en": "Digestive tract surgeon, trained at UFPE in 1984",
        "es": "Cirujano del aparato digestivo, formado en la UFPE en 1984",
    },
    "Cirurgião da Rede Dor São Luiz, Unimed, Américas Santa Joana": {
        "en": "Surgeon at Rede D'Or São Luiz, Unimed and Américas Santa Joana",
        "es": "Cirujano de Rede D'Or São Luiz, Unimed y Américas Santa Joana",
    },
    "Oncologista do Einstein Hospital Israelita": {
        "en": "Oncologist at Hospital Israelita Albert Einstein",
        "es": "Oncólogo del Hospital Israelita Albert Einstein",
    },
    "Especialista em Cirurgia Geral e Coloproctologia": {
        "en": "Specialist in general surgery and coloproctology",
        "es": "Especialista en cirugía general y coloproctología",
    },
    "Memorial São José/Star e Unimed": {
        "en": "Memorial São José/Star and Unimed",
        "es": "Memorial São José/Star y Unimed",
    },
    "Oncologista Clínico da Rede D’Or e Gerente Médico do IDOR Pernambuco": {
        "en": "Clinical oncologist at Rede D'Or and medical manager of IDOR Pernambuco",
        "es": "Oncólogo clínico de Rede D'Or y gerente médico del IDOR Pernambuco",
    },
    "Formado pelo ICESP/USP": {
        "en": "Graduate of ICESP/USP",
        "es": "Formado por el ICESP/USP",
    },
    "Cirurgião do Aparelho Digestivo e transplante de fígado pela FAMERP.": {
        "en": "Digestive tract and liver transplant surgeon, trained at FAMERP.",
        "es": "Cirujano del aparato digestivo y de trasplante hepático por la FAMERP.",
    },
    "Mestrado em cirurgia pela FAMERP.": {
        "en": "Master's degree in surgery from FAMERP.",
        "es": "Maestría en cirugía por la FAMERP.",
    },
    "Proctor de cirurgia robótica pelo Colégio Brasileiro de Cirurgiões e Intuitive surgical.": {
        "en": "Robotic surgery proctor for the Brazilian College of Surgeons and Intuitive Surgical.",
        "es": "Proctor de cirugía robótica por el Colegio Brasileño de Cirujanos e Intuitive Surgical.",
    },
    "Responsável pelo programa de transplante hepático robótico dos hospitais: 9 de julho e beneficência portuguesa.": {
        "en": "Lead for the robotic liver transplant programme at Hospital 9 de Julho and Beneficência Portuguesa.",
        "es": "Responsable del programa de trasplante hepático robótico de los hospitales 9 de Julho y Beneficência Portuguesa.",
    },
    "Médico do serviço de Medicina Nuclear do Hospital Santa Joana e do setor de": {
        "en": "Physician in the Nuclear Medicine service at Hospital Santa Joana and in the",
        "es": "Médico del servicio de Medicina Nuclear del Hospital Santa Joana y del sector de",
    },
    "PET/CT do Hospital Memorial Star e da clínica CEMUPE.": {
        "en": "PET/CT service at Hospital Memorial Star and at Clínica CEMUPE.",
        "es": "PET/CT del Hospital Memorial Star y de la clínica CEMUPE.",
    },
    "Coordenador da Residência de medicina nuclear do Hospital IMIP": {
        "en": "Coordinator of the nuclear medicine residency at Hospital IMIP",
        "es": "Coordinador de la Residencia de Medicina Nuclear del Hospital IMIP",
    },
    "Oncologista clínico RedeDor, IMIP e Hospital Barao de Lucena": {
        "en": "Clinical oncologist at Rede D'Or, IMIP and Hospital Barão de Lucena",
        "es": "Oncólogo clínico de Rede D'Or, IMIP y Hospital Barão de Lucena",
    },
    "Cirurgião do Aparelho Digestivo": {
        "en": "Digestive tract surgeon",
        "es": "Cirujano del aparato digestivo",
    },
    "Atuação em cirurgia Hepato-Bileo-Pancreática": {
        "en": "Practice in hepato-pancreato-biliary surgery",
        "es": "Actuación en cirugía hepato-bilio-pancreática",
    },
    "Huoc/ imip/ Hosp Santa Joana": {
        "en": "HUOC / IMIP / Hospital Santa Joana",
        "es": "HUOC / IMIP / Hospital Santa Joana",
    },
    "Coordenador Oncologia Clínica do Hospital do Câncer de Pernambuco": {
        "en": "Clinical oncology coordinator at Hospital do Câncer de Pernambuco",
        "es": "Coordinador de Oncología Clínica del Hospital do Câncer de Pernambuco",
    },
    "Oncologista Clínico do Imip, Santa Joana e Unionco": {
        "en": "Clinical oncologist at IMIP, Santa Joana and Unionco",
        "es": "Oncólogo clínico del IMIP, Santa Joana y Unionco",
    },
    "Mestre pelo IMIP": {
        "en": "Master's degree from IMIP",
        "es": "Magíster por el IMIP",
    },
    "Oncologista clínico do hospital Santa Joana Recife e da clínica professor Antônio Figueira Filho.": {
        "en": "Clinical oncologist at Hospital Santa Joana Recife and Clínica Professor Antônio Figueira Filho.",
        "es": "Oncólogo clínico del Hospital Santa Joana Recife y de la clínica Professor Antônio Figueira Filho.",
    },
    "Mestre em medicina pela UPE.": {
        "en": "Master's degree in medicine from UPE.",
        "es": "Magíster en medicina por la UPE.",
    },
    "Doutorando em medicina translacional -UNIFESP -SP.": {
        "en": "PhD candidate in translational medicine – UNIFESP, São Paulo.",
        "es": "Doctorando en medicina traslacional – UNIFESP, São Paulo.",
    },
    "Especialista em oncologia mamária pelo MD Anderson Cancer Center, Houston/TX, EUA. Especialização em tumores ginecológicos pela Escola de Tumores Ginecológicos do Instituto Oncoclínicas.": {
        "en": "Specialist in breast oncology at MD Anderson Cancer Center, Houston, Texas, USA. Specialist training in gynaecological tumours at the Gynaecological Tumour School of Instituto Oncoclínicas.",
        "es": "Especialista en oncología mamaria por el MD Anderson Cancer Center, Houston, Texas, EE. UU. Especialización en tumores ginecológicos por la Escuela de Tumores Ginecológicos del Instituto Oncoclínicas.",
    },
    "Professor assistente de oncologia mamária da disciplina de mastologia da UPE-PE": {
        "en": "Assistant professor of breast oncology in the breast surgery course at UPE, Pernambuco",
        "es": "Profesor asistente de oncología mamaria de la disciplina de mastología de la UPE, Pernambuco",
    },
    "Membro da regional norte e nordeste de Coloproctologia": {
        "en": "Member of the North and Northeast regional branch of Coloproctology",
        "es": "Miembro de la regional Norte y Nordeste de Coloproctología",
    },
    "Membro da Sociedade Brasileira de Coloproctologia": {
        "en": "Member of the Brazilian Society of Coloproctology",
        "es": "Miembro de la Sociedad Brasileña de Coloproctología",
    },
    "Coloproctologista da Endograstro": {
        "en": "Colorectal surgeon at Endograstro",
        "es": "Coloproctóloga de Endograstro",
    },
    "Cirurgião Hepatobiliar e Cientista, Policlinico Universitario Gemelli (Roma) - Professor Assistente, Universidade Católica do Sagrado Coração - Pesquisador Sênior, IRCAD França": {
        "en": "Hepatobiliary surgeon and scientist, Policlinico Universitario Gemelli (Rome) – assistant professor, Università Cattolica del Sacro Cuore – senior researcher, IRCAD France",
        "es": "Cirujana hepatobiliar y científica, Policlinico Universitario Gemelli (Roma) – profesora asistente, Universidad Católica del Sagrado Corazón – investigadora sénior, IRCAD Francia",
    },
    "Graduada em Nutrição pela UNINASSAU": {
        "en": "Degree in nutrition from UNINASSAU",
        "es": "Graduada en nutrición por la UNINASSAU",
    },
    "Atuante em Nutrição Clínica hospitalar": {
        "en": "Practising in inpatient clinical nutrition",
        "es": "Actúa en nutrición clínica hospitalaria",
    },
    "Atualmente Nutricionista Oncológica no Hospital Santa Joana Recife": {
        "en": "Currently an oncology dietitian at Hospital Santa Joana Recife",
        "es": "Actualmente nutricionista oncológica en el Hospital Santa Joana Recife",
    },
    "Preceptora da residencia de clínica medica do HSJ Recife": {
        "en": "Preceptor of the internal medicine residency at HSJ Recife",
        "es": "Preceptora de la residencia de clínica médica del HSJ Recife",
    },
    "Preceptora da residencia de endocrinologia do IMIP": {
        "en": "Preceptor of the endocrinology residency at IMIP",
        "es": "Preceptora de la residencia de endocrinología del IMIP",
    },
    "Doutora pela UFPE": {
        "en": "PhD from UFPE",
        "es": "Doctora por la UFPE",
    },
    "Membro do departamento de lipodistrofia da ABESO e membro eleito do departamento de dislipidemia da SBEM": {
        "en": "Member of the lipodystrophy department of ABESO and elected member of the dyslipidaemia department of SBEM",
        "es": "Integrante del departamento de lipodistrofia de la ABESO e integrante electa del departamento de dislipidemia de la SBEM",
    },
    "Residência em Oncologia Clínica pelo IMIP-PE": {
        "en": "Residency in clinical oncology at IMIP, Pernambuco",
        "es": "Residencia en oncología clínica por el IMIP-PE",
    },
    "Oncologista clínico do Hospital Santa Joana": {
        "en": "Clinical oncologist at Hospital Santa Joana",
        "es": "Oncólogo clínico del Hospital Santa Joana",
    },
    "Oncologista clínico do Hospital Universitário Oswaldo Cruz - Universidade de Pernambuco": {
        "en": "Clinical oncologist at Hospital Universitário Oswaldo Cruz – University of Pernambuco",
        "es": "Oncólogo clínico del Hospital Universitário Oswaldo Cruz – Universidad de Pernambuco",
    },
    "Membro ASCO, ESMO e SBOC e GBOT": {
        "en": "Member of ASCO, ESMO, SBOC and GBOT",
        "es": "Miembro de ASCO, ESMO, SBOC y GBOT",
    },
    "Mestre e doutor em Cirurgia pela Universidade de Pernambuco (UPE). Atua como cirurgião geral no Hospital Otávio de Freitas, onde também exerce atividades de preceptoria de residentes e estudantes de Medicina. Possui experiência em cirurgia gastroenterológica e formação complementar em cirurgia robótica e cirurgia minimamente invasiva.": {
        "en": "Master's degree and PhD in surgery from the University of Pernambuco (UPE). General surgeon at Hospital Otávio de Freitas, where he also precepts residents and medical students. Experienced in gastrointestinal surgery, with further training in robotic surgery and minimally invasive surgery.",
        "es": "Magíster y doctor en cirugía por la Universidad de Pernambuco (UPE). Actúa como cirujano general en el Hospital Otávio de Freitas, donde también ejerce la preceptoria de residentes y estudiantes de medicina. Tiene experiencia en cirugía gastroenterológica y formación complementaria en cirugía robótica y cirugía mínimamente invasiva.",
    },
    "Médico gastrohepatologista e Coordenador do Instituto do fígado do Hospital Santa Joana.": {
        "en": "Gastro-hepatologist and coordinator of the Liver Institute at Hospital Santa Joana.",
        "es": "Médico gastrohepatólogo y coordinador del Instituto del Hígado del Hospital Santa Joana.",
    },
    "Médico hepatologista do IMIP": {
        "en": "Hepatologist at IMIP",
        "es": "Médico hepatólogo del IMIP",
    },
    "Professor de Gastroenterologia da Faculdade de Ciências Médicas - PB": {
        "en": "Professor of gastroenterology at Faculdade de Ciências Médicas – Paraíba",
        "es": "Profesor de gastroenterología de la Faculdade de Ciências Médicas – Paraíba",
    },
    "Coordenador do serviço de Medicina Nuclear e PET/CT do IMIP": {
        "en": "Coordinator of the Nuclear Medicine and PET/CT service at IMIP",
        "es": "Coordinador del servicio de Medicina Nuclear y PET/CT del IMIP",
    },
    "Médico Nuclear dos Hospitais Santa Joana e Memorial Star": {
        "en": "Nuclear medicine physician at Hospital Santa Joana and Hospital Memorial Star",
        "es": "Médico nuclear de los hospitales Santa Joana y Memorial Star",
    },
    "Residência em Endoscopia e Fellowship em Endoscopia Avançada pelo HC-FMUSP": {
        "en": "Residency in endoscopy and fellowship in advanced endoscopy at HC-FMUSP",
        "es": "Residencia en endoscopia y fellowship en endoscopia avanzada por el HC-FMUSP",
    },
    "Preceptor da residência médica de endoscopia do IMIP": {
        "en": "Preceptor of the endoscopy residency at IMIP",
        "es": "Preceptor de la residencia médica de endoscopia del IMIP",
    },
    "Endoscopista Colaborador da Endogastro (Hospital Santa Joana)": {
        "en": "Collaborating endoscopist at Endogastro (Hospital Santa Joana)",
        "es": "Endoscopista colaborador de Endogastro (Hospital Santa Joana)",
    },
}
