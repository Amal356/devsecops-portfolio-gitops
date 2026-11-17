#!/usr/bin/env python3
"""Étape 213 : promotion GitOps SANS reconstruire l'image.

Copie le bloc « images: » (noms, tags et DIGESTS) d'un environnement vers le suivant.
Seul Git change : Argo CD déploie ensuite exactement la même image signée.

    python3 scripts/promouvoir.py dev staging
    python3 scripts/promouvoir.py staging prod
"""
import re, sys

ORDRE = ["dev", "staging", "prod"]
src, dst = sys.argv[1], sys.argv[2]
if ORDRE.index(dst) != ORDRE.index(src) + 1:
    sys.exit(f"Promotion refusée : {src} -> {dst} (ordre obligatoire : dev -> staging -> prod)")

def bloc_images(texte):
    m = re.search(r"^images:\n(?:  .*\n|#.*\n)+", texte, re.M)
    if not m:
        sys.exit("bloc images: introuvable")
    return m

t_src = open(f"envs/{src}/kustomization.yaml").read()
p_dst = f"envs/{dst}/kustomization.yaml"
t_dst = open(p_dst).read()
m_src, m_dst = bloc_images(t_src), bloc_images(t_dst)
t_dst = t_dst[:m_dst.start()] + m_src.group(0) + t_dst[m_dst.end():]
open(p_dst, "w").write(t_dst)
for nom, tag, digest in re.findall(r"newName: (\S+)\n\s+newTag: \"([^\"]+)\"\n\s+digest: (\S+)", m_src.group(0)):
    print(f"{dst}: {nom.split('/')[-1]}:{tag} @ {digest[:19]}…")
