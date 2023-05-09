import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  server:{
    proxy:{
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      }
    }
  },
  build: {
    outDir: '/home/kyle/Desktop/sei-course/project2/server/static',
    emptyOutDir: true,
    
  },
  plugins: [react()],
})
