
<h1>Pyges project</h1>
<p>A CMS for Pyramid and Google App Engine</p>

<a href="${request.route_url('create_page')}">Create new page</a>
<br><br>
<a href="${request.route_url('upload')}">Upload new photo</a>
<br><br>
Created pages:
<ul>
	% for page in pages:
		<li><a href="/view_page/${page.key().id()}">${page.title}</a></li>
	% endfor
</ul>

Uploaded photos:
<ul>
	% for foto in imatges:
		<li><a href="/view_picture/${foto.key().id()}">${foto.titol}</li>
	% endfor
</ul>
