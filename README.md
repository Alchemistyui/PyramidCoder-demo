
## Pyramid Coder Demo

This is a demo for paper "Pyramid Coder: Hierarchical Code Generator for Compositional Visual Question Answering".

## Project Setup

```sh
cd ./PyramidCoder-demo/
npm install
```

### Install other packages needed

```sh
npm install --save-dev @vitejs/plugin-vue
npm install axios
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Run the server

```sh
cd server/
python server.py
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Run with docker

```sh
docker-compose up --build
```
