import pytest
from django.core.urlresolvers import reverse

from liqd_product.apps.mapideas import phases
from tests.factories import PhaseFactory
from tests.helpers import assert_template_response
from tests.helpers import freeze_phase
from tests.helpers import setup_phase
from tests.helpers import setup_users

from .factories import MapIdeaFactory


def setup_mapidea_moderation():
    phase, module, project, item = setup_phase(PhaseFactory, MapIdeaFactory,
                                               phases.FeedbackPhase)
    anonymous, moderator, initiator = setup_users(project)
    with freeze_phase(phase):
        url = reverse(
            'liqd_product_mapideas:mapidea-moderate',
            kwargs={
                'partner_slug': item.project.organisation.partner.slug,
                'pk': item.pk,
                'year': item.created.year
            })
        return anonymous, moderator, initiator, url


@pytest.mark.django_db
def test_moderator_has_access(client):
    anonymous, moderator, initiator, url = setup_mapidea_moderation()
    assert client.login(username=moderator.email, password='password')
    resp = client.get(url)
    assert_template_response(
        resp,
        'liqd_product_mapideas/mapidea_moderate_form.html'
    )


@pytest.mark.django_db
def test_initiator_has_access(client):
    anonymous, moderator, initiator, url = setup_mapidea_moderation()
    assert client.login(username=initiator.email, password='password')
    resp = client.get(url)
    assert_template_response(
        resp,
        'liqd_product_mapideas/mapidea_moderate_form.html'
    )


@pytest.mark.django_db
def test_anonymount_has_no_access(client):
    anonymous, moderator, initiator, url = setup_mapidea_moderation()
    resp = client.get(url, follow=True)
    assert_template_response(resp, 'account/login.html')