import { provinces } from './data.js';

function renderProvinces() {
  const container = document.getElementById('provinces-container');
  if (!container) return;

  container.innerHTML = provinces.map(item => `
    <article class="province-card" data-id="${item.id}">
      <div class="province-img-wrap">
        <img src="${item.image}" alt="${item.name}" loading="lazy" />
      </div>
      <div class="province-body">
        <h3 class="province-name">${item.name}</h3>
        <p class="province-desc">${item.desc}</p>
        <a href="collection.html?region=${item.id}" class="province-link">Explore More</a>
      </div>
    </article>
  `).join('');
}

document.addEventListener('DOMContentLoaded', () => {
  renderProvinces();
});