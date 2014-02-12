
<h1>Pyges project</h1>
<p>A CMS for Pyramid and Google App Engine</p>

<a href="${request.route_url('create_page')}">Create new page</a>
<br />
<a href="${request.route_url('trans_menu')}">Translates menu</a>
<br><br>
Choose the language:
<select name="main_lang">
% for l in langs:
	<option value="${l}">${langs[l]}</option>
% endfor
</select>
<br><br>

Created pages:
<ul>
	% for page in pages:
		<li><a href="/view_page/${page.key().id()}">${page.title}</a> - ${langs[page.lang]}</li>
	% endfor
</ul>

