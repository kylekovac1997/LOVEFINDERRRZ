import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  server:{
    proxy:{
      '/api': 'http://localhost:5000/'
    }
  },
  build: {
    rollupOptions: {
      external: ['react-is']
    }
  },
  plugins: [react()],
})
