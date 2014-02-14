<html>
	<head>
		<!--<link rel="stylesheet" href="/static/main.css" type="text/css">-->
		<style>
			${contingut}
		</style>
	</head>
	<body>
		<div class="header">
			<%block name="header">
				<form action="" method="post">
					<select name="skinselect">
						% for skin in listskins:
							<option value="${skin.id}">${skin.nom}</option>
						% endfor
					</select>
					<input type="submit" value="Canvia skin"/>
				</form>
			
				<div id="centeredmenu">
				<ul>
				% for pagina in pages:
					% if pagina.key().id() == page.key().id():
						<li><a href="/view_page/${pagina.key().id()}" class="active">${pagina.title}</a></li>
					% elif pagina.key().id() != page.key().id():
						<li><a href="/view_page/${pagina.key().id()}">${pagina.title}</a></li>
					% endif
				% endfor
				</ul>
				</div>
			</%block>
		</div>
		<div class="content">
			${self.body()}
		</div>
		<div class="footer">
			<%block name="footer">
				<div class="botog ">Footer</div>
				<div class="botog boto2">Footer</div>
				<div class="botog boto2">Footer</div>
				<div class="botog boto2">Footer</div>
				<div class="botog boto2">Footer</div>
				<br/>		
			</%block>	
		</div>
	</body>
</html>
