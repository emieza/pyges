
<h1>Pyges: contact page</h1>

<form method="post">
	First name:<br>
	<input type="text" name="firstname" /><br>
	Second name:<br>
	<input type="text" name="surname" /><br>
	Text:<br>
	<textarea name="text" rows="8" cols="80"></textarea><br>
	<input type="submit" value="Send">
</form>
% if missatge:
	${missatge} 
	
% endif
