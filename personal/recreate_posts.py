from blogengine.models import Post

with open('posts', 'r') as f:
    a = f.read()
posts = a.split('5555555555555')
for i in posts:
    try:
        text = i.split('&&')[1]
        tt = i.split('&&')[0]
    except Exception:
        import pdb; pdb.set_trace()
    if not text or not tt:
        import pdb; pdb.set_trace()
    title = tt.split('\n')[0]
    print title
    if not title:
       print tt, "tt"
       import pdb; pdb.set_trace()
    teaser = tt.split('\n')[1].replace('\n', '')
    slug = '-'.join(title.lower().replace(
        '\r', '').replace(';', '').replace('.', '').replace(',', '').replace('!', '').replace(':', '').split(' '))
    if not (slug or title or text or teaser):
       import pdb; pdb.set_trace()
    try:
        p = Post.objects.create(slug=slug, text=text,
            title=title, teaser=teaser)
        # p = Post.objects.create(slug=slug, text_en=text,
        #    title_en=title, teaser_en=teaser)
    except:
        import pdb; pdb.set_trace()
