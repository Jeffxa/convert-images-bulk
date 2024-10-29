# Terminal app

This terminal convert images to webp or avif, And you can resize and compress
you images with custom parameters.

All yours images would in images folder in the root.

## Steps

1. Clone this repository
2. Run this comand  for install requirements:
```
pip install -r requirements.txt
```
3. See the list command with:
```
python app.py --help
```
4. Command example
```
python app.py -f avif -s 800 -c 50 -d 1
```
5. This command make the follow: 
- Convert to avif formant.
- Resize to 800px width and mantain the proportion.
- Compress to 50%.
- Delete all original files.

Visit my website: [JeffersonEspinoza.com](https://jeffersonespinoza.com).