##base.mako
<%inherit file="base.mako"/>
<%block name="header">
	this is some header content
</%block>
this is body content

<h1>Pyges: view page</h1>

<h2>${page.title}</h2>

<div>${page.text}</div>

<br>
<a href="/">Return home</a>.
