import pytest

from meinberlin.apps.dashboard2 import components
from meinberlin.apps.documents.phases import CommentPhase
from meinberlin.test.helpers import assert_template_response
from meinberlin.test.helpers import setup_phase

component = components.modules.get('document_settings')


@pytest.mark.django_db
def test_edit_view(client, phase_factory):
    phase, module, project, item = setup_phase(
        phase_factory, None, CommentPhase)
    initiator = module.project.organisation.initiators.first()
    url = component.get_base_url(module)
    client.login(username=initiator.email, password='password')
    response = client.get(url)
    assert_template_response(
        response, 'meinberlin_documents/document_dashboard.html')