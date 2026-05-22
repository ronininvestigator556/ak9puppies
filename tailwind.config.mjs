/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        midnight: "#0D0D0D",
        graphite: "#1B1B1B",
        gold: "#B08D57",
        ivory: "#F2F2F2",
        stone: "#A3A3A3",
      },
      fontFamily: {
        heading: ["Cinzel", "Georgia", "serif"],
        body: ["Inter", "system-ui", "sans-serif"],
      },
      boxShadow: {
        soft: "0 18px 60px rgb(0 0 0 / 0.28)",
        gold: "0 0 0 1px rgb(176 141 87 / 0.22), 0 18px 50px rgb(0 0 0 / 0.24)",
      },
    },
  },
  plugins: [],
};
