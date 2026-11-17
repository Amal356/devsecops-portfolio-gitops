# devsecops-portfolio-gitops

Dépôt **GitOps** du DevSecOps Portfolio (activité 8 de M. Wahid, ISET Tozeur).
Il ne contient **que** les manifests Kubernetes : Argo CD le surveille et applique automatiquement
chaque commit dans le cluster K3s. Le code de l'application est dans
[Amal356/cv-devsecops](https://github.com/Amal356/cv-devsecops).

```text
base/                 manifests communs (Kustomize) : API, frontend, PostgreSQL, Ingress
envs/dev/             DEV      – namespace portfolio-dev      – 1 replica
envs/staging/         STAGING  – namespace portfolio-staging  – 2 replicas
envs/prod/            PROD     – namespace portfolio-prod     – 3 replicas, limites API plus élevées
scripts/promouvoir.py promotion d'une image (même digest) : dev -> staging -> prod
```

- Images : Harbor `localhost:8090/devsecops/*`, **signées avec Cosign** et fixées par **digest** ;
  Kyverno refuse toute image non signée.
- Une Application Argo CD par dossier `envs/*` est générée par l'**ApplicationSet** `portfolio`.
- Promotion sans reconstruire l'image : `python3 scripts/promouvoir.py dev staging`, commit, push.
- Aucun secret dans ce dépôt : `postgres-credentials`, `api-secrets` et `harbor-pull` sont créés dans chaque namespace.
