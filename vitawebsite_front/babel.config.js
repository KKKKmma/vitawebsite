module.exports = {
  presets: ["@vue/cli-plugin-babel/preset"],
};

module.exports = {
  devServer: {
    proxy: {
      "^/api/": {
        target: "http://127.0.0.1:8000/api/",
        ws: false,
      },
    },
  },
  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: "./dist/",
  // assetsDir must match Django's STATIC_URL
  assetsDir: "static",
};

const path = require("path");

module.exports = {
  entry: "./index.js",
  output: {
    filename: "index.bundle.js",
    path: path.resolve(__dirname, "./"),
  },
};
