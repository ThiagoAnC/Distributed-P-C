<?php
	/* handle-submit.php */
	header('Content-Type: application/json');

	if(isset($_POST['username']) && !empty($_POST['username'])){
		$name = $_POST['username'];
	}
	if(isset($_POST['pass']) && !empty($_POST['pass'])){
		$email = $_POST['pass'];
	}

	if ($name && $email) {
		$response = $arrayName = array(
			'username' => $username,
			'pass' => $pass,
		);
		echo json_encode($response);
	}
?>