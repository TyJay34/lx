<?php
/*
 * Rで出力したヒートマップのカーペット情報(carpet)をエクセル表示可能な形にする
 */

//入力ファイルを読み込む
$input = '/media/link2/file/TJ/labo/oged/pf_site2/ppf/result_clustring_carpet.txt';

//ファイル名に日本語が入っているとき
//$input = mb_convert_encoding($file_path,'SJIS','UTF-8');


$file = file ( $input );

//出力ファイルを指定
//$output = mb_convert_encoding($file_path,'SJIS','UTF-8');
$output = '/media/link2/file/TJ/labo/oged/pf_site2/ppf/narabi.tsv';

//前処理
$str = "carpet";
$count = 0;
$tmp = "";
$flag = false;

//carpetはあらかじめ転置した状態として処理を行う
//これはRでcarpetをt(h$carpet)として出力すれば良い


/*
 * 縦軸を取得（糖転移酵素）
 */
foreach ( $file as $line ) {
	$tmp = preg_split ( "/ +/", $line );

	if ($tmp [0] === "") {
		if ($flag === false) {
			$flag = true;
		} else {
			break;
		}
	}
	$vertical_array [] = $tmp [0];
}

/*
 * 横軸（生物名）と成分（プロファイル情報）取得
 */
foreach ( $file as $line ) {

	$tmp = preg_split ( "/ +/", $line );

	$count = count ( $tmp );

	//横軸取得
	if ($tmp [0] === "") {
		array_shift ( $tmp );
		{
			foreach ( $tmp as $value ) {
				$holizon_array [] = trim ( $value );
			}
		}
		$vertical_index = 0;
	}

	//成分取得
	else {
		$vertical_index ++;
		array_shift ( $tmp );

		foreach ( $tmp as $value ) {
			$vertical_array [$vertical_index] .= "\t" . trim ( $value );
		}
	}
}

//横軸出力
foreach ( $holizon_array as $line ) {
	$str .= "\t" . $line;
}

$str = trim ( $str );

//縦軸および成分の出力
foreach ( $vertical_array as $line ) {
	$str .= $line . "\n";
}

//120607 上の処理では最後に上下が逆になっているので最後に上下を逆順にする以下の処理を追加
//ヘッダ（生物名の部分）を保護
$str_array = explode ( "\n", $str );
$str = array_shift ( $str_array ) . "\n";

//配列を逆に
$revers_str_array = array_reverse ( $str_array );

foreach ( $revers_str_array as $line ) {
	if ($line !== "") {
		$str .= $line . "\n";
	}
}

echo 'carpet.php ended.';

file_put_contents ( $output, $str );
