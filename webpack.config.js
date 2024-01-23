const path = require('path');

module.exports = {
  entry: './web_src/index.js', // Entry point
  output: {
    filename: 'bundle.js', // Output file name
    path: path.resolve(__dirname, 'static'), // Output directory
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Apply rule to .js files
        exclude: /node_modules/, // Exclude node_modules directory
        use: {
          loader: 'babel-loader', // Use Babel loader for transpiling JavaScript
          options: {
            presets: ['@babel/preset-env'], // Babel preset for modern JavaScript
          },
        },
      },
    ],
  },
};
