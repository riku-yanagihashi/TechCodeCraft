/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.{js,css}",
    "./app/**/*.py"
  ],
  theme: {
    extend: {
      zIndex: {
        '-1': '-1',
      }
    }
  },
  variants: {},
  plugins: [],
}

