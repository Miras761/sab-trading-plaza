// SAB Trading Plaza — Main JS

// Auto-hide messages after 4 seconds
document.addEventListener('DOMContentLoaded', () => {
  const msgs = document.querySelectorAll('.msg');
  msgs.forEach(msg => {
    setTimeout(() => {
      msg.style.transition = 'opacity 0.5s';
      msg.style.opacity = '0';
      setTimeout(() => msg.remove(), 500);
    }, 4000);
  });

  // Image preview on file select
  const fileInputs = document.querySelectorAll('input[type="file"]');
  fileInputs.forEach(input => {
    input.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file || !file.type.startsWith('image/')) return;

      let preview = input.parentElement.querySelector('.img-preview');
      if (!preview) {
        preview = document.createElement('div');
        preview.className = 'img-preview';
        preview.style.cssText = 'margin-top:10px; width:80px; height:80px; border-radius:10px; overflow:hidden; border:2px solid rgba(0,255,136,0.4);';
        const img = document.createElement('img');
        img.style.cssText = 'width:100%; height:100%; object-fit:cover;';
        preview.appendChild(img);
        input.parentElement.appendChild(preview);
      }
      const img = preview.querySelector('img');
      img.src = URL.createObjectURL(file);
    });
  });

  // Char counter for textareas
  document.querySelectorAll('textarea[maxlength]').forEach(ta => {
    const max = ta.getAttribute('maxlength');
    const counter = document.createElement('div');
    counter.style.cssText = 'font-size:0.75rem; color:var(--text-muted); text-align:right; margin-top:4px; font-family:"Share Tech Mono",monospace;';
    counter.textContent = `0 / ${max}`;
    ta.parentElement.appendChild(counter);
    ta.addEventListener('input', () => {
      const len = ta.value.length;
      counter.textContent = `${len} / ${max}`;
      counter.style.color = len > max * 0.9 ? '#f87171' : 'var(--text-muted)';
    });
  });

  // Brainrot select + custom name toggle
  const brainrotSelect = document.querySelector('select[name="brainrot"]');
  const customNameInput = document.querySelector('input[name="custom_brainrot_name"]');
  if (brainrotSelect && customNameInput) {
    brainrotSelect.addEventListener('change', () => {
      if (brainrotSelect.value) {
        customNameInput.style.opacity = '0.4';
        customNameInput.placeholder = 'Выбран брейнрот из списка';
      } else {
        customNameInput.style.opacity = '1';
        customNameInput.placeholder = 'Или введите имя вручную...';
      }
    });
    customNameInput.addEventListener('input', () => {
      if (customNameInput.value) {
        brainrotSelect.style.opacity = '0.4';
      } else {
        brainrotSelect.style.opacity = '1';
      }
    });
  }

  // Matrix rain effect on hero
  const heroEl = document.querySelector('.hero');
  if (heroEl) createMatrixRain(heroEl);
});

function createMatrixRain(container) {
  const canvas = document.createElement('canvas');
  canvas.style.cssText = 'position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; opacity:0.07; z-index:0;';
  container.style.position = 'relative';
  container.insertBefore(canvas, container.firstChild);

  const ctx = canvas.getContext('2d');
  const resize = () => {
    canvas.width = container.offsetWidth;
    canvas.height = container.offsetHeight;
  };
  resize();
  window.addEventListener('resize', resize);

  const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ🧠';
  const fontSize = 13;
  let columns = Math.floor(canvas.width / fontSize);
  const drops = Array(columns).fill(1);

  setInterval(() => {
    ctx.fillStyle = 'rgba(2, 12, 6, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#00ff88';
    ctx.font = `${fontSize}px "Share Tech Mono", monospace`;
    columns = Math.floor(canvas.width / fontSize);
    while (drops.length < columns) drops.push(1);

    for (let i = 0; i < columns; i++) {
      const char = chars[Math.floor(Math.random() * chars.length)];
      ctx.fillText(char, i * fontSize, drops[i] * fontSize);
      if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
      drops[i]++;
    }
  }, 60);
}
