<?php
require_once __DIR__ . '/../config/db.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit('Método no permitido');
}

$i1 = isset($_POST['i1']) ? (int)$_POST['i1'] : 0;
$i2 = isset($_POST['i2']) ? (int)$_POST['i2'] : 0;
$i3 = isset($_POST['i3']) ? (int)$_POST['i3'] : 0;

$i1 = $i1 ? 1 : 0;
$i2 = $i2 ? 1 : 0;
$i3 = $i3 ? 1 : 0;

$stmt = $pdo->prepare("INSERT INTO inputs (i1, i2, i3) VALUES (?, ?, ?)");
$stmt->execute([$i1, $i2, $i3]);

echo "OK";
?>
