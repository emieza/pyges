<h1>Pyges: view translate</h1>

<ul>
    % for page in pages:
        <li><a href="/create_trans/${page.key().id()}">${page.title}</a> - ${langs[page.lang]}</li>
        % if page.jump:
        	<br />
        % endif
    % endfor
</ul>

<br>
<a href="/">Return home</a>.
