
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
	% for picture in pictures:
		<li><a href="/view_picture/${picture.key().id()}">${picture.title}</li>
	% endfor
</ul>

<a href="${request.route_url('view_all_images')}">View all images</a>
