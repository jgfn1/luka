#!/usr/bin/env python3
"""English and Spanish strings for the scientific programme.

Keys are the Portuguese strings exactly as `generate_content.pretty()` renders
them, so a change to the CSV that is not translated here fails loudly instead
of silently shipping Portuguese inside the English page.
"""

LABELS = {
    "Presidente": {"en": "Chair", "es": "Presidente"},
    "Moderadores": {"en": "Moderators", "es": "Moderadores"},
    "Chairman": {"en": "Chairman", "es": "Chairman"},
    "Discussão": {"en": "Discussion", "es": "Discusión"},
    "ABERTURA": {"en": "OPENING", "es": "APERTURA"},
    "ENCERRAMENTO": {"en": "CLOSING", "es": "CIERRE"},
    "COFFEE BREAK": {"en": "COFFEE BREAK", "es": "COFFEE BREAK"},
    "ALMOÇO": {"en": "LUNCH", "es": "ALMUERZO"},
    "A definir": {"en": "To be confirmed", "es": "Por confirmar"},
    "Online": {"en": "Online", "es": "En línea"},
    "Itália": {"en": "Italy", "es": "Italia"},
    "Mesa": {"en": "Panel", "es": "Mesa"},
    "1 hora e 30 min": {"en": "1 h 30 min", "es": "1 h 30 min"},
    "10 min": {"en": "10 min", "es": "10 min"},
    "15 min": {"en": "15 min", "es": "15 min"},
    "20 min": {"en": "20 min", "es": "20 min"},
    "30 min": {"en": "30 min", "es": "30 min"},
    "45 min": {"en": "45 min", "es": "45 min"},
}

ROLES = {
    "Oncologista": {"en": "Clinical Oncologist", "es": "Oncólogo Clínico"},
    "Oncologista Clínico": {"en": "Clinical Oncologist", "es": "Oncólogo Clínico"},
    "Cirurgião": {"en": "Surgeon", "es": "Cirujano"},
    "Cirurgiã": {"en": "Surgeon", "es": "Cirujana"},
    "Cirurgião Oncológico": {"en": "Surgical Oncologist", "es": "Cirujano Oncólogo"},
    "Cirurgião Geral": {"en": "General Surgeon", "es": "Cirujano General"},
    "Cirurgião Abdominal": {"en": "Abdominal Surgeon", "es": "Cirujano Abdominal"},
    "Cirurgião Vascular": {"en": "Vascular Surgeon", "es": "Cirujano Vascular"},
    "Cirurgião Hepatobiliar": {"en": "Hepatobiliary Surgeon", "es": "Cirujano Hepatobiliar"},
    "Coloproctologista": {"en": "Colorectal Surgeon", "es": "Coloproctólogo"},
    "Hepatologista": {"en": "Hepatologist", "es": "Hepatólogo"},
    "Gastro Hepatologista": {"en": "Gastro-Hepatologist", "es": "Gastro-Hepatólogo"},
    "Gastroenterologista": {"en": "Gastroenterologist", "es": "Gastroenterólogo"},
    "Radiologista": {"en": "Radiologist", "es": "Radiólogo"},
    "Patologista": {"en": "Pathologist", "es": "Patólogo"},
    "Radioterapeuta": {"en": "Radiation Oncologist", "es": "Radioncólogo"},
    "Medicina Nuclear": {"en": "Nuclear Medicine", "es": "Medicina Nuclear"},
    "Nutricionista": {"en": "Dietitian", "es": "Nutricionista"},
    "Nutróloga": {"en": "Nutrition Physician", "es": "Nutrióloga"},
    "Enfermeira": {"en": "Nurse", "es": "Enfermera"},
    "Endocrinologista": {"en": "Endocrinologist", "es": "Endocrinólogo"},
    "Preparador Físico": {"en": "Exercise Physiologist", "es": "Preparador Físico"},
}

TITLES = {
    # ── Mesas ──
    "Multidisciplinaridade em tumores Gastrointestinais": {
        "en": "Multidisciplinary care in gastrointestinal tumours",
        "es": "Multidisciplinariedad en tumores gastrointestinales",
    },
    "Esôfago e Estômago — Doença Localizada": {
        "en": "Oesophagus and Stomach — Localised Disease",
        "es": "Esófago y Estómago — Enfermedad Localizada",
    },
    "Câncer Gástrico Avançado": {
        "en": "Advanced Gastric Cancer",
        "es": "Cáncer Gástrico Avanzado",
    },
    "Tumores câncer de pâncreas": {
        "en": "Pancreatic cancer",
        "es": "Cáncer de páncreas",
    },
    "Carcinoma Hepatocelular": {
        "en": "Hepatocellular Carcinoma",
        "es": "Carcinoma Hepatocelular",
    },
    "Câncer colorretal – diagnóstico e patologia": {
        "en": "Colorectal cancer – diagnosis and pathology",
        "es": "Cáncer colorrectal – diagnóstico y patología",
    },
    "Câncer de reto": {"en": "Rectal cancer", "es": "Cáncer de recto"},
    "Metástase hepáticas e câncer de vias biliares": {
        "en": "Liver metastases and biliary tract cancer",
        "es": "Metástasis hepáticas y cáncer de vías biliares",
    },
    # ── Dia 1 ──
    "Sarcopenia e caquexia, da triagem ao plano nutricional": {
        "en": "Sarcopenia and cachexia: from screening to the nutrition plan",
        "es": "Sarcopenia y caquexia: del cribado al plan nutricional",
    },
    "Câncer, metabolismo e novas drogas: obesidade, diabetes e GLP-1 no paciente oncológico": {
        "en": "Cancer, metabolism and new drugs: obesity, diabetes and GLP-1 in the cancer patient",
        "es": "Cáncer, metabolismo y nuevos fármacos: obesidad, diabetes y GLP-1 en el paciente oncológico",
    },
    "A importância da atividade física no tratamento oncológico": {
        "en": "The role of physical activity in cancer treatment",
        "es": "La importancia de la actividad física en el tratamiento oncológico",
    },
    "Navegação em tumores GI: barreiras, adesão e continuidade do cuidado": {
        "en": "Patient navigation in GI tumours: barriers, adherence and continuity of care",
        "es": "Navegación en tumores GI: barreras, adherencia y continuidad del cuidado",
    },
    "Microbioma no câncer GI: evidência atual e limites para aplicação clínica": {
        "en": "The microbiome in GI cancer: current evidence and limits for clinical use",
        "es": "Microbioma en el cáncer GI: evidencia actual y límites para la aplicación clínica",
    },
    "Biomarcadores no câncer gástrico: quais resultados podem mudar a estratégia?": {
        "en": "Biomarkers in gastric cancer: which results can change the strategy?",
        "es": "Biomarcadores en el cáncer gástrico: ¿qué resultados pueden cambiar la estrategia?",
    },
    "Cirurgia ou preservação de órgão no CEC de esôfago: seleção, vigilância e resgate": {
        "en": "Surgery or organ preservation in oesophageal SCC: selection, surveillance and salvage",
        "es": "Cirugía o preservación de órgano en el CEC de esófago: selección, vigilancia y rescate",
    },
    "Imunoterapia no câncer gástrico e de junção ressecável: evidências e seleção de pacientes": {
        "en": "Immunotherapy in resectable gastric and junctional cancer: evidence and patient selection",
        "es": "Inmunoterapia en el cáncer gástrico y de unión resecable: evidencia y selección de pacientes",
    },
    "Caso Clínico: neoplasia da junção esofagogástrica e do estômago — doença localizada": {
        "en": "Clinical case: gastro-oesophageal junction and stomach cancer — localised disease",
        "es": "Caso clínico: neoplasia de la unión esofagogástrica y del estómago — enfermedad localizada",
    },
    "Primeira linha de CG metastático: como os biomarcadores definem o tratamento?": {
        "en": "First line in metastatic GC: how biomarkers define treatment",
        "es": "Primera línea en CG metastásico: ¿cómo definen los biomarcadores el tratamiento?",
    },
    "Adenocarcinoma gástrico avançado CPS <10 e Claudina 18.2 +: Eu faço QT+Imuno": {
        "en": "Advanced gastric adenocarcinoma CPS &lt;10 and Claudin 18.2+: I choose chemo + immunotherapy",
        "es": "Adenocarcinoma gástrico avanzado CPS &lt;10 y Claudina 18.2+: Yo indico QT + inmunoterapia",
    },
    "Adenocarcinoma gástrico avançado CPS <10 e Claudina 18.2 +: Eu faço QT+Zolbetuximabe": {
        "en": "Advanced gastric adenocarcinoma CPS &lt;10 and Claudin 18.2+: I choose chemo + zolbetuximab",
        "es": "Adenocarcinoma gástrico avanzado CPS &lt;10 y Claudina 18.2+: Yo indico QT + zolbetuximab",
    },
    "Cirurgia na doença metastática: quem selecionar, com qual objetivo e quais limites?": {
        "en": "Surgery in metastatic disease: whom to select, with which goal and which limits?",
        "es": "Cirugía en la enfermedad metastásica: ¿a quién seleccionar, con qué objetivo y qué límites?",
    },
    "Ressecabilidade no câncer de pâncreas: além da anatomia, quem é candidato à cirurgia?": {
        "en": "Resectability in pancreatic cancer: beyond anatomy, who is a surgical candidate?",
        "es": "Resecabilidad en el cáncer de páncreas: más allá de la anatomía, ¿quién es candidato a cirugía?",
    },
    "Insuficiência pancreática pós-cirúrgica: como manejar": {
        "en": "Post-surgical pancreatic insufficiency: how to manage it",
        "es": "Insuficiencia pancreática posquirúrgica: cómo manejarla",
    },
    "Caso Clínico — cirurgia inicial ou neoadjuvância: como escolher a estratégia e quando operar?": {
        "en": "Clinical case — upfront surgery or neoadjuvant therapy: how to choose and when to operate?",
        "es": "Caso clínico — cirugía inicial o neoadyuvancia: ¿cómo elegir la estrategia y cuándo operar?",
    },
    "Carcinoma hepatocelular BCLC A: eu indico tratamentos ablativos — para quem e por quê?": {
        "en": "Hepatocellular carcinoma BCLC A: I recommend ablative treatment — for whom and why?",
        "es": "Carcinoma hepatocelular BCLC A: yo indico tratamientos ablativos — ¿para quién y por qué?",
    },
    "Carcinoma hepatocelular BCLC A: eu indico cirurgia — para quem e por quê?": {
        "en": "Hepatocellular carcinoma BCLC A: I recommend surgery — for whom and why?",
        "es": "Carcinoma hepatocelular BCLC A: yo indico cirugía — ¿para quién y por qué?",
    },
    "Transplante hepático após imunoterapia no carcinoma hepatocelular: seleção de pacientes, riscos e benefícios": {
        "en": "Liver transplantation after immunotherapy in hepatocellular carcinoma: patient selection, risks and benefits",
        "es": "Trasplante hepático tras inmunoterapia en el carcinoma hepatocelular: selección de pacientes, riesgos y beneficios",
    },
    # ── Dia 2 ──
    "Cólon localmente avançado: cirurgia inicial ou neoadjuvância?": {
        "en": "Locally advanced colon cancer: upfront surgery or neoadjuvant therapy?",
        "es": "Colon localmente avanzado: ¿cirugía inicial o neoadyuvancia?",
    },
    "Imunoterapia no câncer de cólon: onde se encaixa em cada estágio?": {
        "en": "Immunotherapy in colon cancer: where does it fit at each stage?",
        "es": "Inmunoterapia en el cáncer de colon: ¿dónde encaja en cada estadio?",
    },
    "Alvos moleculares no câncer colorretal: do resultado do teste à escolha terapêutica": {
        "en": "Molecular targets in colorectal cancer: from the test result to the treatment choice",
        "es": "Dianas moleculares en el cáncer colorrectal: del resultado de la prueba a la elección terapéutica",
    },
    "Impacto da radiologia na avaliação de resposta ao tratamento": {
        "en": "The impact of radiology on treatment response assessment",
        "es": "Impacto de la radiología en la evaluación de respuesta al tratamiento",
    },
    "Terapia neoadjuvante e imunoterapia — Como estamos?": {
        "en": "Neoadjuvant therapy and immunotherapy — where are we?",
        "es": "Terapia neoadyuvante e inmunoterapia — ¿cómo estamos?",
    },
    "Seguimento do paciente após Watch and Wait: como conduzir?": {
        "en": "Patient follow-up after Watch and Wait: how to manage it?",
        "es": "Seguimiento del paciente tras Watch and Wait: ¿cómo conducirlo?",
    },
    "Ressecção multivisceral no câncer de reto: indicações e limites": {
        "en": "Multivisceral resection in rectal cancer: indications and limits",
        "es": "Resección multivisceral en el cáncer de recto: indicaciones y límites",
    },
    "Atualização em colangiocarcinoma: imunoterapia e oncodrivers": {
        "en": "Update on cholangiocarcinoma: immunotherapy and oncodrivers",
        "es": "Actualización en colangiocarcinoma: inmunoterapia y oncodrivers",
    },
    "Preservação de parênquima hepático nas cirurgias para metástases hepáticas — o que há de novo": {
        "en": "Liver parenchyma preservation in surgery for liver metastases — what is new",
        "es": "Preservación del parénquima hepático en las cirugías para metástasis hepáticas — qué hay de nuevo",
    },
    "Estratégias não cirúrgicas no tratamento local metástases hepáticas": {
        "en": "Non-surgical strategies for the local treatment of liver metastases",
        "es": "Estrategias no quirúrgicas en el tratamiento local de metástasis hepáticas",
    },
    "Conferência — Transplante Hepático Robótico: a Nova Fronteira da Cirurgia Minimamente Invasiva?": {
        "en": "Lecture — Robotic Liver Transplantation: the New Frontier of Minimally Invasive Surgery?",
        "es": "Conferencia — Trasplante Hepático Robótico: ¿la Nueva Frontera de la Cirugía Mínimamente Invasiva?",
    },
    # ── Simpósios satélites ──
    "Simpósio Satélite — Servier": {
        "en": "Satellite Symposium — Servier",
        "es": "Simposio Satélite — Servier",
    },
    "Simpósio Satélite — AstraZeneca": {
        "en": "Satellite Symposium — AstraZeneca",
        "es": "Simposio Satélite — AstraZeneca",
    },
    "Simpósio Satélite — Bristol (HCC)": {
        "en": "Satellite Symposium — Bristol (HCC)",
        "es": "Simposio Satélite — Bristol (HCC)",
    },
    "Simpósio Satélite — Roche": {
        "en": "Satellite Symposium — Roche",
        "es": "Simposio Satélite — Roche",
    },
    "Simpósio Satélite — Daiichi": {
        "en": "Satellite Symposium — Daiichi",
        "es": "Simposio Satélite — Daiichi",
    },
}


def lookup(table: dict, text: str, lang: str) -> str:
    """Translate `text`, or return it unchanged for Portuguese."""
    if lang == "pt" or not text:
        return text
    entry = table.get(text)
    if entry is None:
        raise KeyError(f"tradução ausente ({lang}): {text!r}")
    return entry[lang]
