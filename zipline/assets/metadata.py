#
# Copyright 2015 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class AssetMetaDataSource(object):

    cache = {}
    fields = ("asset_type",
              "symbol",
              "asset_name",
              "start_date",
              "end_date",
              "first_traded",
              "exchange",
              "notice_date",
              "expiration_date",
              "contract_multiplier")

    def __iter__(self):
        return self.cache.__iter__()

    def read(self):
        return self.cache.itervalues()

    def retrieve_metadata(self, sid):
        return self.cache.get(sid)

    def insert_metadata(self, sid, **kwargs):

        entry = self.retrieve_metadata(sid)
        if entry is None:
            entry = {}

        entry['sid'] = sid
        for key, value in kwargs.iteritems():
            if key in self.fields:
                entry[key] = value

        self.cache[sid] = entry
