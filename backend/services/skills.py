KNOWN_SKILLS = [
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Linux",
    "Git",
    "GitHub",
    "GitHub Actions",
    "Jenkins",
    "Ansible",
    "Python",
    "Prometheus",
    "Grafana",
    "ArgoCD",
    "Helm"
]

def extract_skills(text):
    found = []

    for skill in KNOWN_SKILLS:
        if skill.lower() in text.lower():
            found.append(skill)

    return found
