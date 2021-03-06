# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from django.conf.urls.defaults import patterns, url

from oneanddone.users import views


urlpatterns = patterns('',
    url(r'^profile/$', views.ProfileDetailView.as_view(), name='users.profile.detail'),
    url(r'^profile/new/$', views.CreateProfileView.as_view(), name='users.profile.create'),
    url(r'^profile/edit/$', views.UpdateProfileView.as_view(), name='users.profile.update'),
)
