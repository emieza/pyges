<h1>Pyges: site config</h1>

<form method="post">
	Site name:<br>
% if config:
	<input type="text" name="sitename" value="${config.site_name}" /><br>
	Admin users: (one email address per line)<br>
	<textarea name="adminusers" rows="8" cols="50">${config.admins()}</textarea><br>
% else:
	<input type="text" name="sitename" /><br>
	Admin users: (one email address per line)<br>
	<textarea name="adminusers" rows="8" cols="50"></textarea><br>
% endif
	<input type="submit" value="Send">
</form>
