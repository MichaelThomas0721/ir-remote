const production = !process.env.ROLLUP_WATCH;

module.exports = {
  content: ['./public/index.html', './src/**/*.svelte'],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  future: {
    purgeLayersByDefault: true,
    removeDeprecatedGapUtilities: true,
  },
  daisyui: {
    themes: ["dracula"],
  },
};
