{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
    	<form method="POST">
    		{% csrf_token %}
    		<fieldset class="form-group">
    			<legend class="border-bottom mb-4"></legend>
    			{{ form.as_p }}
    		</fieldset>
    		<div class="form-group">
    			<button class="btn btn-outline-info" type="submit">Sign Up</button>
    		</div>	
    	</form>
    	<div class="border-top pt-3">
    		<small class="text-muted">
    			Already Have An Account? <a class="ml-2" href="#">Sign In</a>
    		</small>
     	</div>
    </div> 
{% endblock content %}