## Pyramid Coder Demo

This is a demo for paper "Pyramid Coder: Hierarchical Code Generator for Compositional Visual Question Answering".


### Run with docker

If you're using Docker, simply run the following command.

```sh
docker-compose up --build
```

## Project Setup

To build from scratch, follow these steps to set up.

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
