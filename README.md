# devsecops-portfolio-gitops

Dépôt **GitOps** du DevSecOps Portfolio (activité 8 de M. Wahid, ISET Tozeur).
Il ne contient **que** les manifests Kubernetes : Argo CD le surveille et applique automatiquement
chaque commit dans le cluster K3s. Le code de l'application est dans
[Amal356/cv-devsecops](https://github.com/Amal356/cv-devsecops).

```text
base/            manifests communs (Kustomize) : API, frontend, PostgreSQL, Ingress
envs/dev/        environnement DEV (namespace portfolio-dev)
```

- Images : Harbor `localhost:8090/devsecops/*`, **signées avec Cosign** et fixées par **digest**.
- Aucun secret dans ce dépôt : `postgres-credentials`, `api-secrets` et `harbor-pull` sont créés dans chaque namespace.
