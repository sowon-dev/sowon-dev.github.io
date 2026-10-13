import urllib.request

try:
    with urllib.request.urlopen('http://localhost:4000/2024/12/08/241209batch-service-restart/') as res:
        html = res.read().decode('utf-8')
        print('HTTP Status:', res.status)
        print('TOC rendered:', 'id="toc"' in html)
        print('Highlight block rendered:', 'class="highlight' in html)
        print('Gutter (line numbers) rendered:', 'class="gutter"' in html)
        print('Clipboard script included:', 'clipboard' in html)
except Exception as e:
    print('Error:', e)
