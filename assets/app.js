function updateDashboard() {
    fetch('api/latest.php?t=' + Date.now())
        .then(res => {
            if (!res.ok) throw new Error('Error en red');
            return res.json();
        })
        .then(data => {
            document.querySelectorAll('.status-dot').forEach((el, i) => {
                const val = [data.i1, data.i2, data.i3][i];
                el.className = 'status-dot' + (val ? ' active' : '');
            });
            document.getElementById('last-update').textContent = 'Última actualización: ' + data.time;
        })
        .catch(err => {
            console.error('Error al actualizar:', err);
        });
}

updateDashboard();
setInterval(updateDashboard, 1000);
