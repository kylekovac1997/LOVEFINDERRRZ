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
    outDir: './server/static',
    emptyOutDir: true,
    rollupOptions: {
      external: ['react-is']
    }
  },
  plugins: [react()],
})
