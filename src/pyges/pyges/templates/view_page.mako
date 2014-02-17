##base.mako
<%inherit file="base.mako"/>
	<h1>${page.title}</h1>
    <h3>${langs[page.lang]}</h3>
	<p>${page.text | n}</p>
	<br>
	<a href="/">Return home</a>
