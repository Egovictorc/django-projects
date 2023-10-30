/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}", "./src/**/*.{html,js}"],
  theme: {

    extend: {
      container: {
        center: true,
      },
      fontFamily: {
        "sans": ['Barlow', "sans-serif"]
      },
    },
  },
  plugins: [],
}

