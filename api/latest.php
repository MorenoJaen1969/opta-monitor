<?php
header('Content-Type: application/json');
header('Cache-Control: no-store');

require_once __DIR__ . '/../config/db.php';

$stmt = $pdo->query("SELECT i1, i2, i3, DATE_FORMAT(created_at, '%H:%i:%s') as time FROM inputs ORDER BY id DESC LIMIT 1");
$row = $stmt->fetch();

if ($row) {
    echo json_encode($row);
} else {
    echo json_encode(['i1' => 0, 'i2' => 0, 'i3' => 0, 'time' => '–']);
}
?>
