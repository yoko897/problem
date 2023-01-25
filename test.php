<?php
// 長針・短針の設定
$short = 23;
$long  = 59;

// 24時間表示　→　12時間表示
$hour   = $short <= 12 ? $short : $short - 12;
$minute = $long;

// 短針の角度取得
$rShort = ($hour * (360 / 12)) + $minute * 1/2;

// 長針の角度取得
$rLong = $minute * (360 / 60);

// 角度取得
$ang = abs($rLong - $rShort);
// 角度が小さいほうを表示
echo min($ang, (360 - $ang));