
<h1>Pyges project</h1>
<p>A CMS for Pyramid and Google App Engine</p>

<a href="${request.route_url('create_page')}">Create new page</a><br/>
<a href="${request.route_url('createskin')}">Create new skin</a><br />
<a href="${request.route_url('editcss')}">Edit skin</a>
<br><br>
Created pages:
<ul>
	% for page in pages:
		<li><a href="/view_page/${page.key().id()}">${page.title}</a></li>
	% endfor
</ul>

