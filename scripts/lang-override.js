// Add missing Chinese translations for Butterfly theme
hexo.on('generateBefore', function () {
  const i18n = this.theme.i18n;

  // Only set if not already present
  if (!i18n.get('page.archives')) {
    i18n.set('page.archives', '归档');
  }

  // Keep search dialog in Chinese — no override needed
});
