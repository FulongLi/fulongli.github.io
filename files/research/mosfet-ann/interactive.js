/* Static, local-only visualisation of the saved ANN run. No live inference. */
(() => {
  'use strict';
  const plot = document.getElementById('plot');
  const branch = document.getElementById('branch');
  const points = document.getElementById('points');
  const status = document.getElementById('status');
  const defaultEye = { x: 1.6, y: 1.6, z: 1.1 };
  let surfaces, metadata;
  let camera = { eye: { ...defaultEye } };
  let ready = false;
  let renderToken = 0;
  const controls = [...document.querySelectorAll('select, input, button')];
  controls.forEach(control => { control.disabled = true; });

  function fail(error) {
    console.error(error);
    document.getElementById('error').hidden = false;
    status.textContent = 'The interactive view is unavailable.';
  }

  async function readJSON(url) {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`${url}: ${response.status}`);
    return response.json();
  }

  function referenceTrace(item, heldOut) {
    const ref = item.reference;
    const indices = ref.held_out.map((value, i) => value === heldOut ? i : -1).filter(i => i >= 0);
    return {
      type: 'scatter3d', mode: 'markers',
      x: indices.map(i => ref.current[i]), y: indices.map(i => ref.temperature[i]),
      z: indices.map(i => ref.voltage[i]),
      name: heldOut ? 'Held-out references' : 'Training references',
      visible: points.checked,
      marker: { size: heldOut ? 4 : 2.5, color: heldOut ? '#d97830' : '#455765', opacity: 1 },
      hovertemplate: 'Current: %{x:.2f} A<br>Temperature: %{y:.1f} °C<br>Reference: %{z:.3f} V<extra>%{fullData.name}</extra>'
    };
  }

  async function render() {
    const token = ++renderToken;
    const item = surfaces[branch.value];
    const scores = metadata.metrics[branch.value];
    const traces = [{
      type: 'surface', x: item.current, y: item.temperature, z: item.voltage,
      name: 'ANN prediction', opacity: 0.78, showscale: false,
      colorscale: [[0, '#c7e8ec'], [0.5, '#42a8b8'], [1, '#146079']],
      hovertemplate: 'Current: %{x:.2f} A<br>Temperature: %{y:.1f} °C<br>ANN: %{z:.3f} V<extra></extra>'
    }, referenceTrace(item, false), referenceTrace(item, true)];
    await Plotly.react(plot, traces, {
      autosize: true, margin: { l: 0, r: 0, t: 8, b: 0 },
      paper_bgcolor: '#fafbfc', font: { family: 'Arial, sans-serif', color: '#30363d', size: 11 },
      showlegend: false, uirevision: 'mosfet-ann-view',
      scene: {
        camera, dragmode: 'orbit', aspectratio: { x: 1.2, y: 1, z: 0.85 },
        xaxis: { title: { text: 'Current (A)' }, backgroundcolor: '#f3f6f8' },
        yaxis: { title: { text: 'Temperature (°C)' }, backgroundcolor: '#f3f6f8' },
        zaxis: { title: { text: 'Voltage (V)' }, backgroundcolor: '#f3f6f8' }
      }
    }, { responsive: true, displaylogo: false, displayModeBar: false, scrollZoom: true });
    if (token !== renderToken) return;
    status.textContent = `${item.title}: ${scores.train_n} training / ${scores.n} held-out points; test RMSE ${scores.rmse.toFixed(3)} V. Signed current and voltage follow the repository tables.`;
    ready = true;
    controls.forEach(control => { control.disabled = false; });
  }

  function setCamera(eye) {
    if (!ready) return;
    camera = { ...camera, eye };
    Plotly.relayout(plot, { 'scene.camera': camera }).catch(fail);
  }
  function zoom(factor) {
    const eye = camera.eye || defaultEye;
    const length = Math.hypot(eye.x, eye.y, eye.z) * factor;
    if (length < 0.6 || length > 8) return;
    setCamera({ x: eye.x * factor, y: eye.y * factor, z: eye.z * factor });
  }
  document.getElementById('reset').addEventListener('click', () => {
    camera = { eye: { ...defaultEye }, center: { x: 0, y: 0, z: 0 }, up: { x: 0, y: 0, z: 1 } };
    setCamera({ ...defaultEye });
  });
  document.getElementById('rotate').addEventListener('click', () => {
    const eye = camera.eye || defaultEye, angle = Math.PI / 8;
    setCamera({ x: eye.x * Math.cos(angle) - eye.y * Math.sin(angle),
      y: eye.x * Math.sin(angle) + eye.y * Math.cos(angle), z: eye.z });
  });
  document.getElementById('zoom-in').addEventListener('click', () => zoom(0.8));
  document.getElementById('zoom-out').addEventListener('click', () => zoom(1.25));
  branch.addEventListener('change', () => render().catch(fail));
  points.addEventListener('change', () => {
    if (ready) Plotly.restyle(plot, { visible: points.checked }, [1, 2]).catch(fail);
  });

  Promise.all([readJSON('surfaces.json'), readJSON('run-metadata.json')])
    .then(async data => {
      [surfaces, metadata] = data;
      if (!window.Plotly) throw new Error('Plotly is unavailable');
      await render();
      plot.on('plotly_relayout', event => {
        if (event['scene.camera']) camera = event['scene.camera'];
      });
      plot.on('plotly_webglcontextlost', () => fail(new Error('WebGL context lost')));
    }).catch(fail);
})();
