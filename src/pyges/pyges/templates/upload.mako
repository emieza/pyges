<h1>Galeria: Puja una imatge</h1>

<form method="post" enctype="multipart/form-data">
	Title:<br>
	<input type="text" name="title" /><br>
	Category:<br>
	<select name="category">
		<option value="nature">nature</option>
		<option value="sport">sport</option>
		<option value="aventure">aventure</option>
		<option value="motor">motor</option>
		<option value="technology">technology</option>
	</select>
	Image:<br>
	<input type="file" name="image" />
	<input type="submit" value="Send">
</form>
