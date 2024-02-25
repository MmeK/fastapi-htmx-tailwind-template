# FastAPI + htmx + tailwindcss + fasthx
## tailwindcss
1. Download binary from [github](https://github.com/tailwindlabs/tailwindcss/releases/latest)
2. Rename binary to tailwind
3. Change permissions to executable
```bash
chmod +x tailwind
```
4. Start the build process
```bash
./tailwind -i ./htmx/static/css/input.css -o ./htmx/static/css/output.css --watch
```
More info at [tailwindcss docs](https://tailwindcss.com/docs/installation).