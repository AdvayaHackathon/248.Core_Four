const CACHE_NAME = 'classroom-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/logins.html',
  '/logint.html',
  '/dashboard.html',
  '/assign.html',
  '/student.html',
  '/style.css',
  '/app.js'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(response => response || fetch(e.request))
  );
});
