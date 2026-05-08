const https = require('https');
const options = { headers: { 'User-Agent': 'Mozilla/5.0' } };
https.get('https://html.duckduckgo.com/html/?q=indian+woman+smiling+professional+portrait+filetype:jpg', options, (res) => {
    let data = '';
    res.on('data', (c) => data += c);
    res.on('end', () => {
        const matches = data.match(/src=\"\/\/external-content\.duckduckgo\.com\/iu\/\?u=([^\"&]+)/g);
        if (matches) {
            console.log(matches.slice(0, 10).map(m => decodeURIComponent(m.split('=')[1])).join('\n'));
        }
    });
});
