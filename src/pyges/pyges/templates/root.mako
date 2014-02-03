
<h1>Pyges project</h1>
<p>A CMS for Pyramid and Google App Engine</p>

<a href="${request.route_url('create_page')}">Create new page</a>
<br />
<a href="${request.route_url('view_trans')}">Translates existing page</a>
<br><br>

Created pages:
<ul>
	% for page in pages:
		<li><a href="/view_page/${page.key().id()}">${page.title}</a> - ${langs[page.lang]}</li>
	% endfor
</ul>

